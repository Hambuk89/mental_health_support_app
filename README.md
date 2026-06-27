<!-- This README Page was created by Aki and Han -->

### Real‑Time Mental Health Support App

Overview 

The Real‑Time Mental Health Support App is a fully developed Flask-based web application designed to provide users with a calming and supportive digital environment for mental wellbeing.
This final version includes complete frontend and backend integration, user authentication, community interaction features, mood tracking, and a consistent mobile‑friendly UI.

### Features Implemented

Core User Features
- Dashboard with quick navigation
- Chat interface (ready for real‑time integration)
- Mood Journal submission + confirmation page
- Community Forum with category‑based discussions
- Q&A Forum
- Self‑Help tools
- User Profile page
- Login / Register system

Admin Features
- Admin‑only login page
- Ability to respond to Q&A forum submissions
- Admin account created manually via Python script

UI/UX Features
- Moss‑green color palette
- White outlined UI components
- Merriweather typography
- Smooth hover animations
- Mobile‑optimized layout
- Clean, minimal interface

### Tech Stack

Frontend: HTML5, CSS3, JavaScript
Chosen for simplicity, full control over UI, and compatibility with Flask.

Backend: Flask (Python)
Lightweight, easy routing, ideal for small‑to‑medium web apps.

Database: SQLite
Auto‑generated, zero‑configuration, perfect for academic prototypes.

Styling: Custom CSS + Merriweather Google Font
Matches the calming mental‑health‑focused design system.

### Installation & Setup

Prerequisites
- Python 3
- pip
- Git

Steps

1. Clone the repository
git clone https://github.com/team/projectname.git
cd projectname

2. Create & activate virtual environment (VS Terminal, Windows PowerShell)
python -m venv venv
venv\Scripts\activate

3. Install dependencies
pip install flask
pip install flask_sqlalchemy
pip install flask_bcrypt

4. Run the Application
python app.py

5. Open in browser
http://127.0.0.1:5000

### How to Use
1. Register or log in
2. Navigate through the dashboard
3. Submit a mood journal entry
4. Explore community categories
5. Ask questions in the Q&A forum (Admin)
6. Chat with AI generated chatbot
7. Access self‑help tools
8. View or update your profile

### The projects Structure:

project/
│
├── app.py
├── extensions.py
├── models.py
├── README.md
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   └── js/
│       ├── chat.js
│       ├── community.js
│       └── QAforum.js
│
└── templates/
    ├── about.html
    ├── admin_login.html
    ├── chat.html
    ├── community.html
    ├── community_category.html
    ├── confirmation.html
    ├── dashboard.html
    ├── journal_page.html
    ├── login.html
    ├── mood.html
    ├── mood_submitted.html
    ├── profile.html
    ├── qa_forum.html
    ├── register.html
    └── self_help.html

### Automatic Database Creation
The application uses SQLite.
The database.db file is not included in the repository.
When the app is run for the first time, Flask automatically creates the database file and initializes all required tables.
No manual setup is required.

### Key Implementation Details

Automatic Database Creation:  
SQLite database (database.db) is auto‑generated on first run using SQLAlchemy.

Admin Account Creation:  
Users can create their own accounts directly through the Register page in the application.
Admin users must be created manually using a Python script inside the app context.

Run the following script inside the project directory:

from app import app
from extensions import db
from models import User

with app.app_context():
    admin = User(
        fullname="Admin",
        age=0,
        gender="Other",
        contact="admin@yoobee.com",
        email="admin@yoobee.com",
        password="admin123",
        role="admin"
    )
    db.session.add(admin)
    db.session.commit()
    print("Admin account created!")

This will create an admin user with elevated permissions.

Consistent UI System:  
All pages follow the moss‑green theme, white outlines, and Merriweather typography.

Modular Code Structure:  
Separate files for routes, models, extensions, templates, and static assets.

### Testing

Manual Testing Performed
- User registration & login
- Mood journal submission
- Community category navigation
- Q&A submission & admin response
- Profile page updates
- Mobile responsiveness

Edge Cases Tested
- Empty form submissions
- Invalid login credentials
- Missing fields in journal entries

### Known Limitations

- Chat is not yet real‑time (WebSockets planned).
- No email verification system.
- Admin creation requires manual script execution.

### Team Contributions
Aki: UI/UX design, frontend templates, backend logic, routing, styling system
Han: Backend logic, frontend templates, database models, routing, styling system

### Future Improvements
- Real‑time chat using WebSockets
- AI‑powered chatbot integration
- Advanced mood analytics
- Community moderation tools
- Accessibility improvements and dark mode

### References
- pandas (for data handling)
- numpy (for numerical operations)
- scikit-learn (for machine learning tasks)
- matplotlib (for plotting)
- seaborn for visualisation
- Flask (main web framework)
- Jinja2 (templating engine - built into Flask)
- Werkzeug (backend utilities - also built into Flask)
