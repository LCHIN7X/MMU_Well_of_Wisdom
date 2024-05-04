from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from auth.models import db
from auth.views import auth
from app.views import views 
from flask_bcrypt import Bcrypt
from flask_uploads import IMAGES, UploadSet, configure_uploads
from flask_login import LoginManager

import os

# ------------------------------- CODE ---------------------------------------------

# Intialize SQLAlchemy database


DATABASE_NAME = "database.db"
bcrypt = Bcrypt()
photos = UploadSet("photos", IMAGES)

# Create function to create app instance
def create_app():
    # create new Flask app and configuring app settings
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "wellofwisdom"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DATABASE_NAME}"
    app.config["UPLOADED_PHOTOS_DEST"] = "static/images"
    app.config["SECRET_KEY"] = os.urandom(24)
    configure_uploads(app, photos)
    db.init_app(app)

    # Registering flask Blueprints
    app.register_blueprint(auth, url_prefix="/auth")
    app.register_blueprint(views) 

    with app.app_context():
        db.create_all()

    return app

# Get the Flask application instance
app = create_app()

if __name__ == "__main__":
    db.create_all
    app.run(debug=True)