<!-- This README Page was created by Aki and Han -->

The Real‑Time Mental Health Support App is an early‑stage prototype designed to provide users with a calming, supportive digital space for mental wellbeing.
This prototype demonstrates the frontend structure, navigation, and visual design of the application using Flask, HTML, and CSS, following the approved style guide from the project proposal (a moss green palette, white outlines, Merriweather typography).

This version of the app represents the Part A prototype of the project, as required in the assignment, and focuses on layout, UI consistency, and page navigation.
Backend functionality and database integration will be added at a later stage.

Features included int this prototype:
    Dashboard, Chat, mood journal, community forum, self help, profile, about, login, register, Q&A forum
(All pages are fully styled and are navigable, as required)

Each page has been designed using the following:
    Green Background, white outlined cards/buttons, merriweather font, consistent hover animations, and a clean app-like layout to fit for a mobile display.
This is to ensure a nice and cohesive user experience that promotes calmness while being aligned with the mental-health theme as is appropriate for our app.

Technologies used:
    Python 3, Flask, HTML5, CSS3, and Merriweather Google Font

The projects Structure:
    project/
    │
    ├── app.py
    ├── README.md
    │
    ├── templates/
    │   ├── dashboard.html
    │   ├── chat.html
    │   ├── mood.html
    │   ├── community.html
    │   ├── self_help.html
    │   ├── profile.html
    │   ├── about.html
    │   ├── login.html
    │   ├── register.html
    │   └── qa_forum.html
    │
    └── static/
        └── css/
            └── style.css

How to RUN the application:
    1. Please create and activate a virtual environment (windows PowerShell) using:
        python -m venv venv
        venv\Scripts\activate

    2. Then install Flask using:
        pip install flask

    3. Proceed to run the app, using the command:
        python app.py

    4. Finally, open in browser using the following:
        http://127.0.0.1:5000
    And the dashboard will then load automatically for display and navigation.