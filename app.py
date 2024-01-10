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
    if int(user_id) > 0:
        user_name = sql_command.getUserName(str(user_id))
    else:
        user_name = None
    return render_template("index.html", user_id = user_id, user_name = user_name)

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
        return redirect(url_for("index", user_id = user_id, user_name = account))

@app.route("/regist", methods = ["POST"])
def regist():
    account = request.form["uname"]
    password = request.form["psw"]

    user_id = sql_command.createUserAccount(account, password)

    if user_id == 0:
        # user_id == -2 -> user used
        return redirect(url_for("index", user_id = -2))
    else:
        return redirect(url_for("index", user_id = user_id, user_name = account))

@app.route("/changeUser/<user_id>", methods = ["POST"])
def changeUser(user_id = 0):
    if user_id == 0:
        return redirect(url_for("index", user_id = -4))
    new_account = request.form["uname"]
    new_password = request.form["psw"]

    original_name = sql_command.getUserName(user_id)
    account_result = sql_command.renameUserAccount(user_id, new_account)
    if account_result == 1:
        password_result = sql_command.resetUserPassword(user_id, new_password)
        if password_result == 0:
            sql_command.renameUserAccount(user_id, original_name)
            return redirect(url_for("index", user_id = -4))
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

# handling searching
@app.route("/searchName/<user_id>/<page>", methods = ["GET", "POST"])
def searchName(page = 1, user_id = 0, keyword = ""):
    addResult = -2
    if request.method == "GET":
        keyword = request.args.get("search")
        addResult = request.args.get("addResult")
    else:
        try:
            keyword = request.form["search"]

            sort_cond = request.form["condition"]
            order = request.form["order"]
            order_bool = True
            if order == "Order":
                order_bool = False
            else:
                order_bool = True
            sql_command.modifySorting(sort_cond, order_bool)
        except:
            keyword = request.args.get("search")

    keywords_list = keyword.replace("[", "").replace("]", "").replace("'", "").split(", ")
    searchResult = sql_command.searchByName(keywords_list)

    page = int(page)
    if page <= 0:
        page = 1
    elif page*10 - len(searchResult) >= 10:
        page -= 1

    searchList = sql_command.takePage(int(page), searchResult)
    searchPage = sql_command.appShortInfo(searchList)

    # just doing the handover
    return render_template(
        "result.html", user_id = user_id, result = searchPage,
          searchWay = "Name", page = int(page), keyword = keyword, addResult = int(addResult))

@app.route("/tag/<user_id>")
def tag(user_id = 0):
    return render_template("search.html", user_id = user_id)

@app.route("/searchTag/<user_id>", methods = ["GET","POST"])
def searchTag(page = 1, user_id = 0):
    page = 1
    addResult = -2
    tags = None
    if request.method == "GET":
        print("Next1")
        tag = request.args.get("search")
        tags = tag.split(";")
        page = int(request.args.get("page"))
        print(page)
        addResult = request.args.get("addResult")
    else:
        try:
            tags = request.form.getlist("tags")
            print("Next2")
            if len(tags) <= 0:
                tag = request.args.get("search")
                page = int(request.args.get("page"))
                print("Next3")
                tags = tag.split(";")

            sort_cond = request.form["condition"]
            order = request.form["order"]
            order_bool = True
            if order == "Order":
                order_bool = False
            else:
                order_bool = True
            sql_command.modifySorting(sort_cond, order_bool)

        except:
            tag = request.args.get("search")
            print(tag)
    print(tags, type(tags))
    searchResult = sql_command.searchByTag(tags)

    page = int(page)
    if page <= 0:
        page = 1
    elif page*10 - len(searchResult) >= 10:
        page -= 1

    searchList = sql_command.takePage(int(page), searchResult)
    searchPage = sql_command.appShortInfo(searchList)

    # just doing the handover
    return render_template(
        "result.html", user_id = user_id, result = searchPage,
          searchWay = "Tag", page = page, keyword = ";".join(tags), addResult = addResult)


# end of handling search
#####################################################################
#####################################################################
# handling add or delete game

@app.route("/addGame", methods = ["GET", "POST"])
def addGame():
    user_id = request.args.get("user_id")
    game_id = request.args.get("game_id")
    searchWay = request.args.get("searchWay")
    keyword = request.args.get("search")
    page = request.args.get("page")

    if int(user_id) <= 0:
        # addResult == 0 -> not login yet
        print("BLOCK")
        if searchWay == "Name":
            return redirect(url_for("searchName", user_id = int(user_id), page = int(page), search = keyword, addResult = 0))
        elif searchWay == "Tag":
            return redirect(url_for("searchTag", user_id = int(user_id), page = int(page), search = keyword, addResult = 0))
        elif searchWay == "Detail":
            return redirect(url_for("gameInfo", user_id = user_id, game_id = game_id, addResult = 0))
    print(str(user_id), str(game_id))
    result = sql_command.insertAppIntoFList(str(user_id), str(game_id))
    if result == 0:
        # addResult == -1 -> failed
        if searchWay == "Name":
            return redirect(url_for("searchName", user_id = int(user_id), page = int(page), search = keyword, addResult = -1))
        elif searchWay == "Tag":
            return redirect(url_for("searchTag", user_id = int(user_id), page = int(page), search = keyword, addResult = -1))
        elif searchWay == "Detail":
            return redirect(url_for("gameInfo", user_id = user_id, game_id = game_id, addResult = -1))
    elif result == 1:
        # addResult == 1 -> success
        if searchWay == "Name":
            return redirect(url_for("searchName", user_id = int(user_id), page = int(page), search = keyword, addResult = 1))
        elif searchWay == "Tag":
            return redirect(url_for("searchTag", user_id = int(user_id), page = int(page), search = keyword, addResult = 1))
        elif searchWay == "Detail":
            return redirect(url_for("gameInfo", user_id = user_id, game_id = game_id, addResult = 1))
@app.route("/deleteGame", methods = ["POST"])
def deleteGame():
    user_id = request.args.get("user_id")
    game_id = request.args.get("game_id")
    print(request.form)

    print(sql_command.showAppFromFList(str(user_id)))
    print("game_id =", game_id)
    result = sql_command.deleteAppFromFList(str(user_id), str(game_id))
    return redirect(url_for("favorite", user_id = int(user_id), page = 1, deleteResult = result))


# end of adding or deleting games
################################################################################
################################################################################
# handling routing of favotite list and game detail

@app.route("/favorite/<user_id>", methods = ["GET", "POST"])
def favorite(user_id = 0):

    favoriteList = None
    if request.method == "POST":
        sort_cond = request.form["condition"]
        order = request.form["order"]
        order_bool = True
        if order == "Order":
            order_bool = False
        else:
            order_bool = True
        sql_command.modifySorting(sort_cond, order_bool)

    favoriteResult = sql_command.showAppFromFList(str(user_id))
    page = int(request.args.get("page"))
    if page <= 0:
        page = 1
    elif page*10 - len(favoriteResult) >= 10:
        page -= 1
    favoriteList = sql_command.takePage(page, favoriteResult)
    favoritePage = sql_command.appShortInfo(favoriteList)

    deleteResult = request.args.get("deleteResult")
    return render_template("wishlist.html", user_id = user_id, wishlist = favoritePage, deleteResult = deleteResult)

@app.route("/gameInfo")
def gameInfo(game_id = 0, user_id = 0):
    user_id = request.args.get("user_id")
    game_id = request.args.get("game_id")
    addResult = request.args.get("addResult")
    print(user_id, game_id)
    game_info = sql_command.appDetailInfo(str(game_id))
    return render_template("game.html", user_id = user_id, game_id = game_id, game_info = game_info, addResult = addResult)

# end of handling routing of favorite list
################################################################################

if __name__ == "__main__":
    # to test on your own pc, change the host to
    # "localhost"
    app.run(debug = True)