from flask import Flask, render_template, request, redirect, url_for, flash
from database_setup import db, User
import bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.secret_key = 'your_secret_key'
db.init_app(app)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # Find the user by username
    user = User.query.filter_by(username=username).first()

    # Check if user exists and if password matches
    if user and bcrypt.checkpw(password.encode(), user.password_hash.encode()):
        return redirect(url_for('success'))
    else:
        flash("Invalid username or password!")
        return redirect(url_for('home'))

@app.route('/success')
def success():
    return render_template('success.html')

@app.route("/hashes")
def show_hashes():
    users = User.query.all()
    return render_template("hashes.html", users=users)

if __name__ == '__main__':
    app.run(debug=True)
