from flask import Flask, render_template

app = Flask(__name__)

# Page routes for the mental health support website (created by Han) #
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/forum')
def forum():
    return render_template('forum.html')

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

if __name__ == '__main__':
    app.run(debug=True)
