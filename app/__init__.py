from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_wtf.csrf import CSRFProtect

# Initialize extensions
db = SQLAlchemy()
bootstrap = Bootstrap()
csrf = CSRFProtect()
DB_NAME = "portfolio.db"

def create_app():
    # Create Flask app instance
    app = Flask(__name__)

    # Application configurations
    app.config['SECRET_KEY'] = 'your_secret_key_here'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions
    db.init_app(app)
    bootstrap.init_app(app)
    csrf.init_app(app)

    # Import and register blueprints or routes
    from .views import views
    app.register_blueprint(views, url_prefix='/')

    return app
