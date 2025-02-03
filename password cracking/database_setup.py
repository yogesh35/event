from flask_sqlalchemy import SQLAlchemy
import bcrypt

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)

    def __init__(self, username, password):
        self.username = username
        # Ensure password is hashed
        self.password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

