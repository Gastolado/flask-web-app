from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

@app.route('/')
def home():
    return "Running..."

@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']

        new_user = User(username=username, email=email)

        db.session.add(new_user)
        db.session.commit()

        return f"Kullanıcı {new_user.username} eklendi!"

    return render_template('add_user.html')

@app.route('/users')
def users():
    all_users = User.query.all()
    user_list = ""
    for user in all_users:
        user_list += f"Username: {user.username}, Email: {user.email}<br>"
    return user_list

if __name__ == '__main__':
    app.run(debug=True)