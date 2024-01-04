# import Flask module
from flask import Flask, render_template, request, url_for

# import hashlib module
import hashlib

# import database module
import db

# assign "static" as the static folder
# Note: the path of D:static and F:app.py is the same
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

