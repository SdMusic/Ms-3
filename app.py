import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from werkzeug.security import generate_password_hash, check_password_hash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/drinks")
def home_page():
    drinks = mongo.db.drinks.find()
    return render_template("drinks.html", drinks=drinks)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Checking if user already exists
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # create new user session cookie
        session["user"] = request.form.get("username").lower()
        flash("You are Registered!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
            else:
                flash("Your Password and/or Username is Incorrect")
                return redirect(url_for("login"))

        else:
            flash("Your Password and/or Username is Incorrect")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("Successful Logout!")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_drink", methods=["GET", "POST"])
def add_drink():
    if request.method == "POST":
        drinks = {
            "category_name": request.form.get("category_name"),
            "drinks_name": request.form.get("drinks_name"),
            "drinks_description": request.form.get("drinks_description"),
            "drinks_method": request.form.get("drinks_method"),
            "created_by": session["user"]
        }
        mongo.db.drinks.insert_one(drinks)
        flash("Great Creation!")
        return redirect(url_for("add_drink"))

    categories = mongo.db.categories.find().sort("category_name", 1),

    return render_template("add_drink.html", categories=categories)


@app.route("/display_drinks.html", methods=["GET"])
def display_drinks():

    cat_gin = mongo.db.cat_gin.find()

    return render_template("display_drinks.html", cat_gin=cat_gin)


@app.route("/drink_recipe/<recipe_id>")
def drink_recipe(recipe_id):
    """
    Recipe Page; brings user to each cocktail's
    own recipe page. searches db for correct
    drink id.
    """
    recipe = mongo.db.drinks.find_one({"idDrink": (recipe_id)})
    return render_template("drink_recipe.html", recipe=recipe)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True)

    