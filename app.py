# import Flask module
from flask import Flask, render_template, request, url_for, redirect

# import hashlib module
import hashlib

# import database module
import sql_command

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
@app.route("/index/<user_id>")
def index(user_id = 0):
    return render_template("index.html", user_id = user_id)

#############################################################
# hadling login problems

# routing of login page
# handling login request
@app.route("/sign", methods = ["POST"])
def sign():
    # for POST request, we should check the user validation
    account = request.form["uname"]
    password = request.form["psw"]
    user_id = sql_command.login(account, password)

    # For a successful login, redirect with user's account.
    # Else redirect to user_id == -1 as failed.
    if user_id == 0:
        return redirect(url_for("index", user_id = -1))
    else:
        return redirect(url_for("index", user_id = user_id))

@app.route("/regist", methods = ["POST"])
def regist():
    account = request.form["uname"]
    password = request.form["psw"]

    user_id = sql_command.createUserAccount(account, password)
    
    if user_id == 0:
        # user_id == -2 -> user used
        return redirect(url_for("index", user_id = -2))
    else:
        return redirect(url_for("index", user_id = user_id))

@app.route("/changeUser/<user_id>", methods = ["POST"])
def change_user_info(user_id):
    new_account = request.form["uname"]
    new_password = request.form["psw"]

    account_result = sql_command.renameUserAccount(user_id, new_account)
    password_result = sql_command.resetUserPassword(user_id, new_password)
    change_result = sql_command.changeUserInfo(user_id, new_account, new_password)
    if change_result == 1:
        # success
    else:
        # failed
        return redirect(url_for("index", user_id = ))

# end of login problems
##################################################################


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
    app.run(debug = True)
