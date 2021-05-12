<img src="design/readme-pic.png" style="margin: auto" />

This website has been created as my data-centric milestone submission for code institutes full stack developer course. [Click](https://milestone3-pf.herokuapp.com/) for the live version. The cocktail database is a collaborative cocktail recipe site with the goal of allowing users to discover new cocktails as well as sharing their own cocktail recipes and ideas.
Users can create their own account with allows them to search the database, add and edit their own cocktails as well as build a personal collection on their profile of their favourite cocktail recipes.

# User Stories
Users of the site should be able to:
- Access this site on any device (mobile, desktop or laptop)
- Browse all cocktail recipes
- View the details of the recipe including ingredients and method
- Add their own cocktail recipes including a URL to show a image of their creations
- Edit their cocktail recipe
- Delete recipes that they have created
- Delete their account
- Be able to log out of their account after using the service 
- Search the database using key words allowing them to search cocktail name, ingredient or category

___

# Design

The site is designed using standard bootstrap with overlaying custom CSS to style the colour scheme. All recipes are displayed on cards showing the image, cocktail name, ingredients and method. Each page contains a matching navigation bar and branded image.

## Framework

- Bootstrap
Is used to provide a clear and modern user interface with minimal need for alteration
- Flask
Flask is used as the templating micro-framework that renders all pages on the site.

## Colour scheme

Colours are based on bootstrap light class and the red #7a1f1f, as with future development i would plan to introduce a dark mode and believe this would a simple yet pleasing aesthetic.

## Wireframes

The wireframes were hand sketched and are available [here]("/design/wireframes")  before being translated in to mockup designs using affinity designer available [here]("/design/mock-ups")

# Features

## Registered user dependant navigation
The nav-bar options that a user will see is dependant on if the user is a logged in user
Users that are not logged in will see:
- Home
- Register
- Log in 
- Drinks list
Logged in users will see:
- Home
- Register
- Log in 
- Drinks list
- Create
- Log Out

## Create account(register)
Users are able to create their own account providing them further access to the site. There is code in pace to check against existing users as to avoid multiples and that password and users names meet minimum and maximum lengths. I have employed the Werkzeug package which take the input from the password form and generates a SHA256 hash that is then stored in the user's profile in MongoDB. This provides far greater security than storing passwords in plain text. 


## User Profile Page 
Once registered or logged in your are directed to your profile, in this area you are able to link to cocktail creation and see your creations and favourites.

## Delete user account.
The user has the ability to remove their account if they no longer wish to be a member of the cocktail database.

## Logout
Users that have logged into the site may end their session at any time by clicking the 'Logout' button on the nav-bar. Flask ends their session using the session.pop() method and redirects the user to the homepage.

## Browse Cocktails

All users are able to broswe the Drinks list containg all drinks in the cocktail database, regardless of wther or not they are registered users or guests. The cocktails are displayed using bootrap cards containing pictures cocktail name, category it is from and a link to view the full recipe.

## Cocktail recipe page.

From the drinks list once the user has selected to view recipe they are take to a page containing the full information of the chosen cocktail if the user is logged in they will also have the option to add the drink to their favourites or if it is already present in their favourited list to remove it from favourties.

## Create Cocktail
Registered users that are logged in will be able to create recipes to be added to the database through this page they are asked to enter
- cocktail name*
- Cocktail descrition*
- Method*
- Image url* (but supplied with a default)
- The glass to serve it in
- Ingredients from 1 to 13 from a drop down or predictive text box and the measure
asterix items are require and from the ingredients  1 and 2 are required before being able to upload.

## Edit Recipe

Once a user has created a recipe they then have the ablity to edit their creations if their username matches the created by field in the database. 

A identical form to the creation page and is populated with the information that was previously entered. Once they have updated these fielfds they are able to click the subit button and the recipe will be updated in the database.

## Delete recipe
User have the option to remove cocktails they have create by clicking the delete button available to them again if their username matches the created_by field in the database,

Once clicked the cocktail is removed from the database and this cannot be undone the cocktail will be removed from their profile and from the database by which removing access for all other users.

## Search fucntion

Users are able to search the database on the drinks list page. They are able to search by keywords for category, drink name and ingredient this is currently a standard mongodb or search function uing text indexs meaning for each word entered it will produce more results. In future development I would change this to a and search.

## Pagination

While displaying cocktails in full list or under search parameters results are restricted to 12 per page, with naviagtion (pagiantion) buttons available
above and below the results.
___

# Technologies Used

- GitPod online IDE
- GitHub - Remote repository for all project code with git version control.

### Front-End Technologies
- HTML - The fundamental code structure for all webpages.
- CSS -  Custom CSS was used for this project to alter the default CSS of the bootstrap framework.
- JavaScript - Used to edit the front-end display
- Bootstrap 5 - Primary visual framework for this project.
- Font Awesome - for icons through out the site
- Affinity suite - Used in planning stage for picture manipulation and mockup design

### Back-End Technologies
- Flask - A templating microframework used to dynamically build the pages in this project.
- Flask paginate - A templating microframework used to dynamically build the pages in this project.
- Jinja 2.10 - HTTP templating language for Python.
- Werkzeug 0.14 - Werkzeug is a comprehensive WSGI web application library. Installed as a dependency of Flask, it provides password hashing and checking for this project.
- Heroku - Hosts the deployed version of this project.
- Python - Python is an interpreted, high-level, general-purpose programming language and is the language used for all backend functions of this project.
- MongoDB Atlas - MongoDB Atlas is the online host for remote MongoDB's NoSQL document-oriented databases.
- PyMongo - PyMongo is a Python distribution containing tools for working with MongoDB.
- Python dotenv - Reads the values of the environmental variables that are set in the project's .env file.
___

## Testing

Due to time constraints, I was  unable to design and implement automatic Unit-testing for this project, and so developer and user manual testing was completed instead. 

### HTML

- Passing the HTML from all templates and base into the [W3C Markup Validator](https://validator.w3.org/) generates numerous errors, but these are expected as the validator is unable to understand the Jinja templating that builds most aspects of the page. For the HTML that does not involve Jinja, no errors have been found.
### CSS

- The CSS has been validatedby passing the CSS through the [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) shows that there are no errors. A no or errors warnings are flagged.
### Javascript

- All Javascript was passes throught the [JSHint Validator](https://jshint.com/) and was found to be syntactically valid.
### Python

- All Python code was passed through the [PEP8 Online](http://pep8online.com/) validator and is fully PEP8 compliant.
### Compatibility

The project was tested to ensure full usability across the following browsers and their mobile equivalents (where applicable):
- Chrome
- Edge
- Firefox
- Opera GX
- Internet Explorer

### Bugs
- Bug 1
Display recipe page displays empty ingredient fields
- Fix 1
Code written that targets the ingredients and changes display to none if the inner html is equal to none
- Bug 2
Pagination for search criteria only showing first page due to search bar no longer containing the search criteria creating a error  $search format = null
-  Fix 2
This was fixed by creating a empty global string variable which is only updated when a search is entered allowing me to set teh value of the variable to the
searchbar allowing the pagination code to run
- Bug 3
Edit page not displaying values in text areas passed in from the edit recipe function
- Fix 3
This issue was easily resolved but took me time as text areas do not have value element and needed to be entered as the html text itself
___

# Deployment

Sign up for a free account on MongoDB and create a new Database . The Collections in that database should be as follows:
	
	users collection containing:
	_id: <ObjectId>
	username: <string>
	password: <string>
	favourite: <array>

	ingredients collection containing:
	_id:<ObjectId>
    idIngredient:<string>
    strIngredient:<string>
    strDescription:<string>
    strType:<string>
    strAlcohol:<string>
    strABV:<string>

	catergories collection containing:
	_id:<ObjectId>
    category_name:<string>

	drinks collection containing from population:
	_id:<ObjectId>
    idDrink:<string>
    strDrink:<string>
    strDrinkAlternate:<string>
    strTags:<string>
    strVideo:<string>
    strCategory:<string>
    strIBA:<string>
    strAlcoholic:<string>
    strGlass:<string>
    strInstructions:<string>
    strInstructionsES:<string>
    strInstructionsDE:<string>
    strInstructionsFR:<string>
    strInstructionsIT<string>
    strInstructionsZH-HANS:<string>
    strInstructionsZH-HANT:<string>
    strDrinkThumb:<string>
    strIngredient1:<string>
    strIngredient2:<string>
    strIngredient3:<string>
    strIngredient4:<string>
    strIngredient5:<string>
    strIngredient6:<string>
    strIngredient7:<string>
    strIngredient8:<string>
    strIngredient9:<string>
    strIngredient10:<string>
    strIngredient11:<string>
    strIngredient12:<string>
    strIngredient13:<string>
    strIngredient14:<string>
    strIngredient15:<string>
    strMeasure1:<string>"
    strMeasure2:<string>
    strMeasure3:<string>
    strMeasure4:<string>
    strMeasure5:<string>
    strMeasure6:<string>
    strMeasure7:<string>
    strMeasure8:<string>
    strMeasure9:<string>
    strMeasure10:<string>
    strMeasure11:<string>
    strMeasure12:<string>
    strMeasure13:<string>
    strMeasure14:<string>
    strMeasure15:<string>
    strImageSource:<string>
    strImageAttribution:<string>
    strCreativeCommonsConfirmed:<string>
    dateModified:<string>
    category_name:<string>
    created_by:<string>

## Creating the Project
This project used the Code Institute's student template. A new repository named ms3-pickyourpoison was created which included all branches from the template.
 The project was developed using the IDE GitPod. Version control software Git was used to commit and push the code to GitHub where it was stored. The following commands were used for this:
- git add filename/directory - This command adds files/directories to the staging area to be committed.
- git commit -m "message here" - This command commits files/directories to the repository. Commit messages should clearly explain the update being committed.
- git push - This command pushes all committed updates/changes into the GitHub repository.

#### Deploying to Heroku
Heroku needs some files to be setup so that it knows what apps and dependencies are needed to run the app.
- use the command "pip3 freeze --local > requirements.txt".
- use the command "echo web: python app.py > Procfile" (ensuring you enter a capital P).
- Add, commit and push.

#### Create Heroku App:
- Create an account or login to Heroku.
- Click on the New button on the top right of your dashboard.
- Select Create new app.
- Enter your new unique app name.
- Choose your region.
- Select Create app.

#### Connect to GitHub Repository:

- On your new app's page, navigate to the Deploy tab.
- Under Deployment method, select GitHub.
- Under Connect to GitHub (and making sure your GitHub profile is displayed), enter the name of your repository and click Search.
- Once your repo has been found, click Connect.

#### Set Environment Variables:
- Navigate to your app's Settings tab.
- Under Config Vars, click Reveal Config Vars.
- You'll need to add the following key:value items;
- key: IP, value: 0.0.0.0
- key: PORT, value: 5000
- key: MONGO_DBNAME, value: (database name you want to connect to)
- key: MONGO_URI, value: (accessed by following the steps below)
- Login to MongoDB.
- Under Data Storage, click Clusters.
- Click Connect on the cluster you want.
- Click Connect your application.
- Copy the link there, replacing < password > with your own one for the database access page, and the database name with the collection/database you want to collect to.
- key: SECRET_KEY, value: (secret key)
- custom and random sequence of characters required for maintaining security.
- generated from RandomKeygen for example.

#### Automatic Deployment:
- Navigate back to your app's Deployment tab.
- Under Automatic deploys, select the branch you wish to deploy from.
- Click Enable Automatic Deploys.

#### Deploying Locally
Please note that the project will not run locally without a new env.py python file being created which contains the following with their corresponding values: IP, PORT, MONGO_DBNAME, MONGO_URI, SECRET_KEY. For security reasons, these details are not included in this repository.

In order to make a clone, follow these steps:

- Log into GitHub.
- Navigate to the Repositories tab.
- Choose the desired repository.
- Above the list of files, click on the Code drop-down menu.
- Copy the clone URL under the HTTPS tab.
- Open a terminal window in your IDE of choice.
- Change the working directory to whichever location you want the cloned directory to be in.
- Type git clone and then paste the URL that you copied earlier.
- Press enter to create the clone.
- In your IDE of choice, type pip install -r requirements.txt in order to install all required packages for project.

## Credits

Content:
- I scraped off the recipes and images to populate the database from
     https://www.thecocktaildb.com/api.php
- favicon is from 
    https://www.favicon-generator.org/search/---/Alcohol
- Missing picture image from: 
    https://www.nationalpetregister.org/assets/img/no-photo.jpg
Code snippets:
- Pagination adapted from:
    https://gist.github.com/mozillazg/69fb40067ae6d80386e10e105e6803c9
- Images
There may images un-accredited in this segment as test users have had access to the project url and therefore 
images may be uploaded that are not contained in this list however their urls to which the credit is due will be available through the app itself.
## Acknowledgements:
	My tutor chris quinn
