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
# user_id {
# 0  : no login
# -1 : incorrect user data
# -2 : user has been used
# -3 : change account success
# -4 : change account failed
# -5 : delete account success
# -6 : delete account failed
# }

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
def changeUser(user_id = 0):
    if user_id == 0:
        return redirect(url_for("index", user_id = -4))
    new_account = request.form["uname"]
    new_password = request.form["psw"]

    account_result = sql_command.renameUserAccount(user_id, new_account)
    if account_result == 1:
        password_result = sql_command.resetUserPassword(user_id, new_password)
    else:
        return redirect(url_for("index", user_id = -4))

    return redirect(url_for("index", user_id = -3))

@app.route("/deleteUser/<user_id>", methods = ["POST"])
def deleteUser(user_id = 0, methods = ["POST"]):
    if user_id == 0:
        return redirect(url_for("index", user_id = 0))
    password = request.form["psw"]
    delete_result = sql_command.deleteUserAccount(user_id, password)
    if delete_result == 0:
        return redirect(url_for("index", user_id = -6))
    else:
        return redirect(url_for("index", user_id = -5))

@app.route("/logout", methods = ["POST"])
def logout():
    return redirect(url_for("index"))

# end of login problems
##################################################################
##################################################################
# handling search

searchResult = None

# handling searching
@app.route("/searchName/<user_id>", methods = ["POST"])
def searchName(page = 1, user_id = 0):
    if page == 1:
        keyword = request.form["search"]
        keywords_list = keyword[1:-1].replace("'", "").split(", ")
        global searchResult
        searchResult = sql_command.searchByName(keywords_list)

    searchPage = sql_command.takePage(page, searchResult)
    # just doing the handover
    return render_template("index.html", user_id = user_id, result = searchPage)

@app.route("/searchTag/<user_id>", methods = ["POST"])
def searchTag(page = 1, user_id = 0):
    searchPage = None
    return render_template("index.html", user_id = user_id, result = searchPage)

# end of handling search
#####################################################################

if __name__ == "__main__":
    # to test on your own pc, change the host to
    # "localhost"
    app.run(debug = True)
