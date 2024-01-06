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
# │  ├─css
# │  ├─icon
# │  └─image
# ├─db.py
# └─app.py

app = Flask(__name__, static_folder = "static")

# routing of home page/ index
@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

# routing of login page
# handling login request
@app.route("/sign", methods = ["GET", "POST"])
def sign():
    if request.method == "GET":
        # for GET request, return the login page
        return render_template("sign.html", fail = False)
    
    elif request.method == "POST":
        # for POST request, we should check the user validation
        account = request.form["uname"]
        password = request.form["psw"]

        # This condition should be modified in future.
        if valid_user(account, password):
            # For a successful login, redirect to home page.
            return redirect(url_for("home", user = account))
        else:
            # For a failed login, redirect to the same page, with modify.
            return render_template("sign.html", fail = True)

# routing for home page
@app.route("/home/<user>")
def home(user):
    return "Hello " + user
    pass 
    return render_template("home.html", user = user)

# a temporary function for user validation
def valid_user(acc, psd):
    return acc == "123" and psd == "456"

# handling searching
@app.route("/search", methods = ["POST"])
def search():
    keyword = request.form["search"]
    keywords = keyword.split(" ")
    # this part should search the result first
    # then uses it as a parameter to render html
    return keywords
    pass
    return render_template("search.html", datas = db.search(keywords))


if __name__ == "__main__":
    # to test on your own pc, change the host to
    # "localhost"
    app.run(debug = True, host = "140.113.89.236", port = 5000)

