#Set up the Flask application and database configuration (By Han)
from flask import Flask, render_template, request, jsonify, session
from extensions import db
from models import User, Question # Importing the Question model for handling questions in the Q&A forum

app = Flask(__name__)

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

@app.route('/chat')
def chat():
    return render_template('chat.html')

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


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

