from flask import Blueprint, render_template, redirect, url_for

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('home.html')


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


@views.route("/portfolio")
def portfolio():
    portfolio_data = [
    "Developed a fully functional role-based authentication system.",
    "Designed optimized database schemas for efficient data storage.",
    "Integrated user-friendly templates with advanced navigation features.",
    "Maintained a comprehensive Git commit history for all projects.",
    ]
    return render_template('portfolio.html', portfolio=portfolio_data)


@views.route("/case_management_system")
def case_management_system():
    case_management_system_data = [
    "Developed a fully functional role-based authentication system.",
    "Designed optimized database schemas for efficient data storage.",
    "Integrated user-friendly templates with advanced navigation features.",
    "Maintained a comprehensive Git commit history for all projects.",
    ]
    return render_template('case_management_system.html', case_management_system=case_management_system_data)

@views.route("/git_tracking_system")
def git_tracking_system():
    git_data = [
    "Developed a fully functional role-based authentication system.",
    "Designed optimized database schemas for efficient data storage.",
    "Integrated user-friendly templates with advanced navigation features.",
    "Maintained a comprehensive Git commit history for all projects.",
    ]
    return render_template('git_tracking_system.html', git_tracking_system=git_data)
    



