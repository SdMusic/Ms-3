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
            "password": generate_password_hash(request.form.get("password")),
            "favourite":"",
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
                return redirect(url_for("profile", username=session['user']))
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
        drinks = mongo.db.drinks.find()
        return render_template("profile.html",
                               username=username,
                               drinks=drinks)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("Successful Logout!")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_drink", methods=["GET", "POST"])
def add_drink():
    if not session.get("user"):
        render_template("templates/error_handlers/404.html")

    if request.method == "POST":
        drinks = {
            "category_name": request.form.get("category_name"),
            "strDrink": request.form.get("drinks_name"),
            "drinks_description": request.form.get("drinks_description"),
            "strInstructions": request.form.get("drinks_method"),
            "strDrinkThumb": request.form.get("img_url"),
            "strGlass": request.form.get("glass"),
            "strIngredient1": request.form.get("ing1"),
            "strIngredient2": request.form.get("ing2"),
            "strIngredient3": request.form.get("ing3"),
            "strIngredient4": request.form.get("ing4"),
            "strIngredient5": request.form.get("ing5"),
            "strIngredient6": request.form.get("ing6"),
            "strIngredient7": request.form.get("ing7"),
            "strIngredient8": request.form.get("ing8"),
            "strIngredient9": request.form.get("ing9"),
            "strIngredient10": request.form.get("ing10"),
            "strIngredient11": request.form.get("ing11"),
            "strIngredient12": request.form.get("ing12"),
            "strIngredient13": request.form.get("ing13"),
            "strIngredient14": request.form.get("ing14"),
            "strIngredient15": request.form.get("ing15"),
            "strMeasure1": request.form.get("measure1"),
            "strMeasure2": request.form.get("measure2"),
            "strMeasure3": request.form.get("measure3"),
            "strMeasure4": request.form.get("measure4"),
            "strMeasure5": request.form.get("measure5"),
            "strMeasure6": request.form.get("measure6"),
            "strMeasure7": request.form.get("measure7"),
            "strMeasure8": request.form.get("measure8"),
            "strMeasure9": request.form.get("measure9"),
            "strMeasure10": request.form.get("measure10"),
            "strMeasure11": request.form.get("measure11"),
            "strMeasure12": request.form.get("measure12"),
            "strMeasure13": request.form.get("measure13"),
            "strMeasure14": request.form.get("measure14"),
            "strMeasure15": request.form.get("measure15"),
            "created_by": session["user"]
        }

        mongo.db.drinks.insert_one(drinks)
        flash("Great Creation!")
        return redirect(url_for("profile", username=session['user']))

    ingredients = mongo.db.ingredients.find()
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template(
        "add_drink.html", categories=categories, ingredients=ingredients)


@app.route("/favourite/<recipe_id>")
def favourite(recipe_id):
    if session["user"]:
        mongo.db.users.update({"username": session["user"]},
            {"$push": {"favourite": recipe_id}})
    return redirect(url_for("profile", username=session['user']))


@app.route("/edit_drink/<recipe_id>", methods=["GET", "POST"])
def edit_drink(recipe_id):
    """
    Edit Cocktail; creator of the recipe can
    edit it. On submit, db will be searched
    for the current recipe by its id. When
    found, recipe in db will be updated
    using the new entries in the edit recipe
    form.
    """
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name"),
            "strDrink": request.form.get("drinks_name"),
            "drinks_description": request.form.get("drinks_description"),
            "strInstructions": request.form.get("drinks_method"),
            "strDrinkThumb": request.form.get("img_url"),
            "strGlass": request.form.get("glass"),
            "strIngredient1": request.form.get("ing1"),
            "strIngredient2": request.form.get("ing2"),
            "strIngredient3": request.form.get("ing3"),
            "strIngredient4": request.form.get("ing4"),
            "strIngredient5": request.form.get("ing5"),
            "strIngredient6": request.form.get("ing6"),
            "strIngredient7": request.form.get("ing7"),
            "strIngredient8": request.form.get("ing8"),
            "strIngredient9": request.form.get("ing9"),
            "strIngredient10": request.form.get("ing10"),
            "strIngredient11": request.form.get("ing11"),
            "strIngredient12": request.form.get("ing12"),
            "strIngredient13": request.form.get("ing13"),
            "strIngredient14": request.form.get("ing14"),
            "strIngredient15": request.form.get("ing15"),
            "strMeasure1": request.form.get("measure1"),
            "strMeasure2": request.form.get("measure2"),
            "strMeasure3": request.form.get("measure3"),
            "strMeasure4": request.form.get("measure4"),
            "strMeasure5": request.form.get("measure5"),
            "strMeasure6": request.form.get("measure6"),
            "strMeasure7": request.form.get("measure7"),
            "strMeasure8": request.form.get("measure8"),
            "strMeasure9": request.form.get("measure9"),
            "strMeasure10": request.form.get("measure10"),
            "strMeasure11": request.form.get("measure11"),
            "strMeasure12": request.form.get("measure12"),
            "strMeasure13": request.form.get("measure13"),
            "strMeasure14": request.form.get("measure14"),
            "strMeasure15": request.form.get("measure15"),
            "created_by": session["user"]
        }
        # correct recipe will be updated using submit dictionary
        mongo.db.drinks.update({"_id": ObjectId(recipe_id)}, submit)
        # Alert user to successful recipe edit
        flash("It's Fixed!")
        return redirect(url_for("profile", username=session['user']))

    # searches db for the correct cocktail recipe by id
    recipe = mongo.db.drinks.find_one({"_id": ObjectId(recipe_id)})
    categories = mongo.db.categories.find()
    return render_template(
        "edit_drink.html", recipe=recipe, categories=categories)


@app.route("/delete_drink/<recipe_id>")
def delete_drink(recipe_id):
    """
    Delete drink; creator of the recipe can
    delete it, from their profile page.
    the cocktail entry is checked and is
    removed from db
    """
    mongo.db.drinks.remove({"_id": ObjectId(recipe_id)})
    # Alert user to successful recipe deletion
    flash("Bye bye, Your Cocktail has been annihilated!!")
    return redirect(url_for("profile", username=session['user']))


@app.route("/display_drinks.html", methods=["GET"])
def display_drinks():

    drinks = mongo.db.drinks.find()

    return render_template(
        "display_drinks.html",
        drinks=drinks)


@app.route("/search", methods=["GET", "POST"])
def search():
    """
    Search bar; user can search by cocktail name or category.
    """
    # pulls input from search bar
    search = request.form.get("search")
    # searches text index
    drinks = mongo.db.drinks.find({"$text": {"$search": search}})
    # displays drinks page with filtered results
    return render_template("display_drinks.html", drinks=drinks)


@app.route("/drink_recipe/<recipe_id>")
def drink_recipe(recipe_id):
    """
    Recipe Page; brings user to each cocktail's
    own recipe page. searches db for correct
    drink id.
    """
    recipe = mongo.db.drinks.find_one({"_id": ObjectId(recipe_id)})
    return render_template("drink_recipe.html", recipe=recipe)


@app.errorhandler(403)
def forbidden(e):
    return render_template("/error_handlers/403.html"), 403


@app.errorhandler(404)
def not_found(e):
    return render_template("/error_handlers/404.html"), 404


@app.errorhandler(500)
def server_error(e):
    return render_template("/error_handlers/500.html"), 500


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
