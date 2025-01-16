from flask import Blueprint, render_template, redirect, url_for

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('home.html')


@views.route('/skills')
def skills():
    skills_data = [
        {"name": "Python", "level": "Intermediate"},
        {"name": "Flask", "level": "Intermediate"},
        {"name": "SQLite", "level": "Intermediate"},
        {"name": "HTML/CSS", "level": "Intermediate"},
        {"name": "Bootstrap", "level": "Intermediate"},
    ]
    return render_template('skills.html', skills=skills_data)

@views.route('/current_projects')
def current_projects():
    projects_data = [
        {
            "title": "Flask Web Application",
            "description": "A role-based Flask app with secure user authentication and dynamic navigation.",
            "link": "https://github.com/yourusername/project1"
        },
        {
            "title": "Document Management System",
            "description": "An upload route with reference number generation and search functionality.",
            "link": "https://github.com/yourusername/project2"
        },
        {
            "title": "User Management System",
            "description": "A system with soft delete functionality and detailed user logs.",
            "link": "https://github.com/yourusername/project3"
        },
    ]
    return render_template('current_projects.html', current_projects=projects_data)


@views.route('/accomplishments')
def accomplishments():
    accomplishments_data = [
        "Developed a fully functional role-based authentication system.",
        "Designed optimized database schemas for efficient data storage.",
        "Integrated user-friendly templates with advanced navigation features.",
        "Maintained a comprehensive Git commit history for all projects.",
    ]
    return render_template('accomplishments.html', accomplishments=accomplishments_data)




