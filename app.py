import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from werkzeug.security import generate_password_hash, check_password_hash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask_paginate import Pagination, get_page_args
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

        # Check that the supplied passwords match
        if request.form.get("password") != request.form.get("confirm_password"):
            flash("Supplied passwords do not match.")
            return render_template("register.html")

        # Create database enty for user
        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "favourite": []
            }
        mongo.db.users.insert_one(register)

        # create new user session cookie
        session["user"] = request.form.get("username").lower()
        flash("You are Registered!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():

    """
    Registered users can log in
    by entering their username and password.
    """
    
    # Confirm if username exists in db
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        # checks if password matches for that user
        if existing_user:
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                # alert user to successful login
                flash("Welcome, {}".format(request.form.get("username")))
                # bring user to their profile after successful login
                return redirect(url_for("profile", username=session['user']))
                # password does not match for that user
            else:
                # alert user to unsuccessful login
                flash("Your Password and/or Username is Incorrect")
                return redirect(url_for("login"))

        # username does not exist in db
        else:
            flash("Your Password and/or Username is Incorrect")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    """
    The session user's username
    pulled from the database and brought to their profile following
    successful login.
    """
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        drinks = mongo.db.drinks.find()
        my_favs = mongo.db.users.find_one(
            {"username": session["user"]})["favourite"]
        my_fav_id = mongo.db.drinks.find({"_id": {"$in": my_favs}})
        # if current session user; user is brought to their profile

        return render_template("profile.html",
                               username=username,
                               drinks=drinks,
                               my_favs=my_favs,
                               my_favs_id=my_fav_id)
    # else redirects user to Log In
    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookie and alert them to succesful log out
    flash("Successful Logout!")
    session.pop("user")
    return redirect(url_for("login"))


@app.route('/delete_profile')
def delete_profile():

    # ----- Check if user and Delete user profile-----

    if session['user']:
        mongo.db.users.remove({'username': session['user']})
        flash('Sorry to see you go!')
        session.pop('user')
        return redirect(url_for("display_drinks"))

    else:
        flash("You do not have the premissions!")
        return redirect(url_for("display_drinks"))


@app.route("/add_drink", methods=["GET", "POST"])
def add_drink():
    """
    A registered user can create
    new recipes. When the user submits
    the creation form, a database entry is created.
    """
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
        # Alert user to successful addition
        flash("Great Creation!")
        return redirect(url_for("profile", username=session['user']))

    ingredients = mongo.db.ingredients.find()
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template(
        "add_drink.html", categories=categories, ingredients=ingredients)


@app.route("/favourite/<recipe_id>")
def favourite(recipe_id):
    """
    Takes the current recipe ID and adds it to the user's
    favourites. Only available as logged in user.
    """
    if "user" in session:
        user = mongo.db.users.find_one({"username": session["user"]})["_id"]
        mongo.db.users.update({"_id": ObjectId(user)},
                              {"$push": {"favourite":
                                         ObjectId(recipe_id)}})
        return redirect(url_for("drink_recipe", recipe_id=recipe_id))
    else:
        flash("You must be logged in to perform that action!")
        return redirect(url_for("drink_recipe", recipe_id=recipe_id))


@app.route("/remove_favourite/<recipe_id>")
def remove_favourite(recipe_id):
    """
    Takes the current recipe ID and removes it from the user's
    favourites. Only available if the favourite exists.
    """
    if "user" in session:
        user = mongo.db.users.find_one({"username": session["user"]})["_id"]
        mongo.db.users.update(
            {"_id": ObjectId(user)},
            {"$pull": {"favourite": ObjectId(recipe_id)}})
        return redirect(url_for("drink_recipe", recipe_id=recipe_id))
    else:
        flash("You must be logged in to perform that action!")
        return redirect(url_for("drink_recipe", recipe_id=recipe_id))


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

    # searches database for the correct cocktail recipe by id
    recipe = mongo.db.drinks.find_one({"_id": ObjectId(recipe_id)})
    categories = mongo.db.categories.find()
    return render_template(
        "edit_drink.html", recipe=recipe, categories=categories)


@app.route("/delete_drink/<recipe_id>")
def delete_drink(recipe_id):
    """
    Creator of the recipe can
    delete it, from their profile page.
    the cocktail entry is checked and is
    removed from database
    """
    mongo.db.drinks.remove({"_id": ObjectId(recipe_id)})
    # Alert user to successful recipe deletion
    flash("Bye bye, Your Cocktail has been annihilated!!")
    return redirect(url_for("profile", username=session['user']))


@app.route("/display_drinks")
def display_drinks():
    """
    Display drink to all users, collects all
    drinks from the drinks collection and
    uses pagination to display 12 per page
    """
    def get_drinks(offset=0, per_page=12):
        # gets drinks list and set pagination parameters
        drinks = mongo.db.drinks.find()
        return drinks[offset: offset + per_page]
    drinks = mongo.db.drinks.find()
    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')
    per_page = 12
    # sets how many results are displayed per page
    total = drinks.count()
    pagination_drinks = get_drinks(offset=offset, per_page=per_page)
    pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='bootstrap4')
    # displays drinks with pagination
    return render_template("display_drinks.html",
                           drinks=pagination_drinks,
                           page=page,
                           per_page=per_page,
                           pagination=pagination,
                           )


searched = ""


@app.route("/search", methods=["GET", "POST"])
def search():
    """
    Search bar; user can search by cocktail name or category.
    """
    # pulls input from search bar
    global searched
    search = request.form.get("search")
    if search is not None:
        searched = search
    else:
        searched = searched
    # searches text index
    drinks = mongo.db.drinks.find({"$text": {"$search": searched}})
    # displays drinks page with filtered results

    def get_drinks(offset=0, per_page=12):
        # gets drinks list and set pagination parameters
        return drinks[offset: offset + per_page]
    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')
    per_page = 12
    # sets how many results are displayed per page
    total = drinks.count()
    pagination_drinks = get_drinks(offset=offset, per_page=per_page)
    pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='bootstrap4')
    # displays drinks with pagination
    return render_template("display_drinks.html",
                           drinks=pagination_drinks,
                           page=page,
                           per_page=per_page,
                           pagination=pagination,
                           search=searched
                           )


@app.route("/drink_recipe/<recipe_id>")
def drink_recipe(recipe_id):
    """
    Recipe Page; brings user to each cocktail's
    own recipe page. searches db for correct
    drink id.
    """
    drinks = mongo.db.drinks.find()
    recipes = mongo.db.drinks.find_one({"_id": ObjectId(recipe_id)})
    # Attempt to retrieve user's favourites as a list
    try:
        favourite = mongo.db.users.find_one(
            {"username": session["user"]})["favourite"]
    except:
        favourite = []
    return render_template("drink_recipe.html",
                           drinks=drinks,
                           favourites=favourite,
                           recipe=recipes)


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
