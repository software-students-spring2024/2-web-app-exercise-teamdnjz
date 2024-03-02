import pymongo
from flask import Flask, render_template, request, make_response
from flask_login import LoginManager, UserMixin, login_user, login_required, current_user, logout_user

login_manager = LoginManager()
app = Flask(__name__)
app.secret_key = "secret"
login_manager.init_app(app)

# Your MongoDB setup
connection = pymongo.MongoClient()
db = connection["star"]

# User model for Flask-Login
class User(UserMixin):
    def __init__(self, userID):
        self.id = userID

@login_manager.user_loader
def load_user(userID):
    return User(userID)

@app.route('/login', methods=['GET'])
def loginGet():
    return render_template("login.html")

@app.route('/login', methods=['POST'])
def loginPost():
    inpUser = request.form['username']
    inpPW = request.form['password']
    user = db.swetest.find_one({'username': inpUser})

    if user and user['password'] == inpPW:
        curUser = User(user['_id'])
        login_user(curUser)
        return render_template("home.html", username = inpUser)
    elif user:
        return render_template("login.html", error = "Incorrect password entered")
    else:
        newUser = {'username': inpUser, 'password': inpPW, 'tasks': []}
        user_id = db.swetest.insert_one(newUser).inserted_id
        curUser = User(user_id)
        login_user(curUser)
        return render_template("home.html", username = inpUser)

if __name__ == "__main__":
    app.run(port="5000")
