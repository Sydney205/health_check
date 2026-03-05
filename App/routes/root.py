from flask import render_template
from App import app
import pandas as pd
import io 



# The root
@app.route('/', methods=["GET", "POST"])
@app.route("/home")
def home():
    return render_template("index.html")


# @app.route("/add_field", methods=["POST"])
# def add_field():
#     name = request.form["field_name"]
#     field_type = request.form["field_type"]
#     fields.append({"name": name, "type": field_type})
#     return redirect(url_for("home"))


# @app.route("/submit_form", methods=["POST"])
# def submit_form():
#     data = request.form
#     return str(data)