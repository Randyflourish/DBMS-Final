# import Flask module
from flask import Flask, render_template, request, url_for, redirect

# import hashlib module
import hashlib

# import database module
# import db

# assign "static" as the static folder
# Note: the path of Dir:static and File:app.py is the same
# DBMS-Final
# ├─ static
# │  ├─ css
# │  ├─ js
# │  ├─ icon
# │  └─ image
# ├─ db.py
# └─ app.py

# simple user database, this will be transplant to sql server
users = ["test1", "test2", "test3"]
user_psw_pairs = {
    "test1" : "123456",
    "test2" : "qwerty",
    "test3" : "1qaz2wsx"
}

app = Flask(__name__, static_folder = "static")

# routing of home page/ index
@app.route("/")
@app.route("/index/<user>")
def index(user = ""):
    return render_template("index.html", user = user)

# routing of login page
# handling login request
@app.route("/sign", methods = ["POST"])
def sign():
    # for POST request, we should check the user validation
    account = request.form["uname"]
    password = request.form["psw"]
    
    # This condition should be modified in future.
    if valid_user(account, password):
        # For a successful login, redirect with user's account.
        return redirect(url_for("index", user = account))
    else:
        # For a failed login, redirect with a null user called Unknown.
        return redirect(url_for("index", user = "Unknown"))

# a temporary function for user validation
def valid_user(acc, psd):
    return acc in users and psd == user_psw_pairs[acc]

# handling searching
@app.route("/search", methods = ["POST"])
def search():
    keyword = request.form["search"]
    keywords = keyword.split(" ")

    # just doing the handover
    return redirect(url_for("result", keywords = keywords))

# rendering searching result
# the main function of searching function
@app.route("/result/<keywords>")
def result(keywords):
    # beware that type(keywords) is string here
    # thus converting to list is necessary
    keywords_list = keywords[1:-1].replace("'", "").split(", ")

    # This should be change into db.search(keywords) later
    return render_template("result.html", keywords = keywords_list)

if __name__ == "__main__":
    # to test on your own pc, change the host to
    # "localhost"
    app.run(debug = True, host = "140.113.89.236", port = 5000)

