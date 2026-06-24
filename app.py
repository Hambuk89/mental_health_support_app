#Set up the Flask application and database configuration (By Han)
from flask import Flask, render_template, request, jsonify, session, redirect
from extensions import db
from models import User, Question, Answer # Importing the Question model for handling questions in the Q&A forum
from datetime import datetime


app = Flask(__name__)
app.secret_key = "mental_health_support_application"


mood_log = []
 
# Configure the SQLite database (By Han)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


# Page routes for the mental health support website (created by Han and Aki) #
@app.route("/")
def home():
    return render_template("dashboard.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/profile')
def profile():

    # Check if user is logged in
    if 'user_id' not in session:
        return redirect('/login')
    
    # Get user info from DB
    user = User.query.get(session['user_id'])

    return render_template('profile.html', user=user)

@app.route('/mood')
def mood():
    return render_template('mood.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # Find user by email
        user = User.query.filter_by(email=email).first()

        # Validate user and password
        if not user or user.password != password:
            return render_template('login.html', error="Invalid email or password.")
        
        # Save login session
        session['user_id'] = user.id
        session['role'] = user.role

        return redirect('/dashboard')

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        fullname = request.form.get('Fullname')
        age = request.form.get('age')
        gender = request.form.get('gender')
        contact = request.form.get('contact')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        # Check if passwords match
        if password != confirm_password:
            return render_template('register.html', error="Wrong Passwords.")
        
        #check for duplicate email
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            return render_template('register.html', error="Email already registered.")
        
        #Create a new user
        new_user = User(
            fullname=fullname,
            age=int(age),
            gender=gender,
            contact=contact,
            email=email,
            password=password,
            role="user"
        )

        db.session.add(new_user)
        db.session.commit()

        return redirect('/login')
    
    return render_template('register.html')

@app.route('/self_help')
def self_help():
    return render_template('self_help.html')

# AI Chat #
@app.route('/chat')
def chat():
    return render_template('chat.html')

@app.route('/send_message', methods=['POST'])  
def send_message():
    data = request.get_json()
    user_message = data.get("message", "")

    ai_response = generate_ai_response(user_message)

    return jsonify({
        "user": user_message,
        "ai": ai_response
    })

def generate_ai_response(user_message):
    return f"AI Response: '{user_message}' Received! How can I help you further?"

@app.route('/community')
def community():
    return render_template('community.html')

@app.route('/admin_login')
def admin_login():
    return render_template('admin_login.html')

@app.route('/Users')
def users():
    all_users = User.query.all()
    return str(all_users)

@app.route("/qa_forum")
def qa_forum():
    role = session.get("role", "user")
    questions = Question.query.order_by(Question.timestamp.desc()).all()
    answers = Answer.query.all()

    return render_template("qa_forum.html", role=role, questions=questions, answers=answers)

@app.route("/submit_question", methods=["POST"])
def submit_question():
    question = request.form.get("question")
    user_id = session.get("user_id")
    new_q = Question(content=question, user_id=user_id)
    db.session.add(new_q)
    db.session.commit()
    print("Received question:", question)
    return jsonify({"success": True})

@app.route("/answer_question/<int:question_id>", methods=['POST'])
def answer_question(question_id):
    # Only admin can answer
    if session.get("role") != "admin":
        return "Unauthorised", 403

    answer_text = request.form.get("answer")
    admin_id = session.get("user_id")

    new_answer = Answer(
        content=answer_text,
        question_id=question_id,
        admin_id=admin_id    
    )

    db.session.add(new_answer)
    db.session.commit()

    return redirect("/qa_forum")


@app.route("/confirm-mood/<mood>", methods=["GET", "POST"])
def confirm_mood(mood):
    return render_template(
        "confirmation.html",
        title="CONFIRM MOOD",
        message=f"Add {mood.upper()} to your journal?",
        confirm_text="Yes, Add Mood!",
        confirm_url=f"/add_mood/{mood}",
        cancel_url="/mood"
    )

@app.route("/add_mood/<mood>", methods=["POST"])
def add_mood(mood):
    # Get comment from form
    comment = request.form.get("comment", "")

    # Create a new moodlog entry
    new_mood = MoodLog(
        mood=mood,
        comment=comment,
        user_id=session.get("user_id") # Link to logged-in user
    )

    db.session.add(new_mood)
    db.session.commit()

    return redirect("/mood-submitted")

@app.route("/my-journal")
def my_journal():
    if "user_id" not in session:
        return redirect("/login")
    
    moods = MoodLog.query.filter_by(user_id=session["user_id"]).order_by(MoodLog.timestamp.desc()).all()


    return render_template("journal_page.html", moods=moods)

@app.route("/mood-submitted")
def mood_submitted():
    return render_template("mood_submitted.html")

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

