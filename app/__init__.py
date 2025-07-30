# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

import os
from dotenv import load_dotenv

load_dotenv()  # 👈 This reads your .env file into environment variables


db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'routes.login'

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'supersecretkey'  # Replace with env var in production
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/projects/resume/site.db'

    db.init_app(app)
    login_manager.init_app(app)

    from app.routes import routes
    app.register_blueprint(routes)

    return app
