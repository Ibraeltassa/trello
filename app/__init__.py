from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = "auth.login"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "supersecretkey"
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///../instance/trello.db"

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    from app import routes, auth, dashboard
    app.register_blueprint(routes.main)
    app.register_blueprint(auth.auth)
    app.register_blueprint(dashboard.dashboard)

    with app.app_context():
        db.create_all()

    return app
