#Set up the Flask application and database configuration (By Han)
from flask import Flask, render_template, request, jsonify, session, redirect
from extensions import db
from models import User, Question # Importing the Question model for handling questions in the Q&A forum
from datetime import datetime

app = Flask(__name__)

mood_log = []
from datetime import datetime
 
# Configure the SQLite database (By Han)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


# Page routes for the mental health support website (created by Han and Aki) #
@app.route("/")
def dashboard():
    return render_template("dashboard.html")

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route("/qa_forum")
def qa_forum():
    role = session.get("role", "user") # Default to "user" if no role is set
    return render_template("qa_forum.html", role=role)

@app.route('/mood')
def mood():
    return render_template('mood.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
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

@app.route("/QA_forum")
def QA_forum():
    return render_template("QA_forum.html")

@app.route("/submit_question", methods=["POST"])
def submit_question():
    question = request.form.get("question")
    new_q = Question(content=question)
    db.session.add(new_q)
    db.session.commit()
    print("Received question:", question)
    return jsonify({"success": True})


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
    timestamp = datetime.now().strftime("%d %B %Y, %I:%M %p")
    comment = request.form.get("comment", "")

    mood_log.append({
        "mood": mood,
        "time": timestamp,
        "comment": comment
    })

    return redirect("/mood-submitted")

@app.route("/my-journal")
def my_journal():
    return render_template("journal_page.html", moods=mood_log)

@app.route("/mood-submitted")
def mood_submitted():
    return render_template("mood_submitted.html")

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

