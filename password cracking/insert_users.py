from database_setup import db, User
from app import app

with app.app_context():
    db.create_all()  # Create tables if they don't exist

    # Insert sample users with hashed passwords
    user1 = User(username="admin", password="password123")
    user2 = User(username="guest", password="guest123")

    # Add users to session
    db.session.add(user1)
    db.session.add(user2)
    
    db.session.commit()  # Commit the transaction

    print("Users inserted!")
