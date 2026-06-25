<!-- This README Page was created by Aki and Han -->

### Real‑Time Mental Health Support App — Final Version
The Real‑Time Mental Health Support App is a fully developed Flask-based web application designed to provide users with a calming and supportive digital environment for mental wellbeing.
This final version includes complete frontend and backend integration, user authentication, community interaction features, mood tracking, and a consistent mobile‑friendly UI.

### The application follows the approved design system:

- Moss‑green color palette
- White outlined UI components
- Merriweather typography
- Smooth hover animations
- Minimal, calming layout optimized for mobile devices

### User Features
- Dashboard with quick navigation
- Chat interface (ready for real‑time integration)
- Mood Journal submission + confirmation page
- Community Forum with category‑based discussions
- Q&A Forum
- Self‑Help tools
- User Profile page
- Login / Register system

### Admin Features
- Admin‑only login page
- Ability to respond to Q&A forum submissions
- Admin account created manually via Python script

### UI/UX Features
- Consistent green theme
- White outlined cards and buttons
- Mobile‑optimized layout
- Smooth hover animations
- Clean, app‑like interface

### Technologies Used
- Backend: Python 3, Flask
- Frontend: HTML5, CSS3, JavaScript
- Database: SQLite (auto‑generated database.db)
- Styling: Merriweather Google Font

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

### User & Admin Accounts
### Regular User Accounts 
Users can create their own accounts directly through the Register page in the application.

### Admin Account Creation
Admin accounts cannot be created through the UI.
They must be created manually using Python.

Run the following script inside the project directory:

from app import app
from extensions import db
from models import User

with app.app_context():
    admin = User(
        username="admin",
        email="admin@example.com",
        password="admin123",
        is_admin=True
    )
    db.session.add(admin)
    db.session.commit()
    print("Admin account created!")

This will create an admin user with elevated permissions.



How to RUN the application:
    1. Please create and activate a virtual environment (windows PowerShell) using:
        python -m venv venv
        venv\Scripts\activate

    2. Then install Flask using:
        pip install flask
        pip install flask_sqlalchemy
        pip install flask_bcrypt

    3. Proceed to run the app, using the command:
        python app.py

    4. Finally, open in browser using the following:
        http://127.0.0.1:5000
    And the dashboard will then load automatically for display and navigation.


### Future Improvements

- Real‑time chat using WebSockets
- AI‑powered chatbot integration
- Advanced mood analytics
- Community moderation tools
- Accessibility improvements and dark mode