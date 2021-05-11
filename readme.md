This website has been created as my data-centric milestone submission for code institutes full stack developer course. The cocktail database is a collaborative cocktail recipe site with the goal of allowing users to discover new cocktails as well as sharing their own cocktail recipes and ideas.
Users can create their own account with allows them to search the database, add and edit their own cocktails as well as build a personal collection on their profile of their favourite cocktail recipes.

User Stories
Users of the site should be able to:
Access this site on any device (mobile, desktop or laptop)
browse all cocktail recipes
view the details of the recipe including ingredients and method
add their own cocktail recipes including a URL to show a image of their creations
edit their cocktail recipe
delete recipes that they have created
delete their account
be able to log out of their account after using the service 
search the database using key words allowing them to search cocktail name, ingredient or category

Design
	The site is designed using standard bootstrap with overlaying custom CSS to style the colour scheme. All recipes are displayed on cards showing the image, cocktail name, ingredients and method. Each page contains a matching navigation bar and branded image.

Framework.
	Bootstrap
	Is used to provide a clear and modern user interface with minimal need for alteration
	Flask
	Flask is used as the templating micro-framework that renders all pages on the site.
Colour scheme
wireframes

Features
	I have implemented the features that are listed in the user stories and additional features to improve the user experience and functionality of the website.

Registered user dependant navigation
	The nav-bar options that a user will see is dependant on if the user is a logged in user
users that are not logged in will see 
	Home
	Register
	Log in 
	Drinks list
Logged in users will see:
	Home
	Register
	Log in 
	Drinks list
	Create
	Log Out

Create account(register)
	Users are able to create their own account providing them further access to the site. There is code in pace to check against existing users as to avoid multiples and that password and users names meet minimum and maximum lengths. I have employed the Werkzeug package which take the input from the password form and generates a SHA256 hash that is then stored in the user's profile in MongoDB. This provides far greater security than storing passwords in plain text. 


User Profile Page 
	Once registered or logged in your are directed to your profile, in this area you are able to link to cocktail creation and see your creations and favourites.

Delete user account.
	The user has the ability to remove their account if they no longer wish to be a member of the cocktail database.

Logout
Users that have logged into the site may end their session at any time by clicking the 'Logout' button on the nav-bar. Flask ends their session using the session.pop() method and redirects the user to the homepage.

Browse Cocktails

All users are able to broswe the Drinks list containg all drinks in the cocktail database, regardless of wther or not they are registered users or guests. The cocktails are displayed using bootrap cards containing pictures cocktail name, category it is from and a link to view the full recipe.

Cocktail recipe page.

From the drinks list once the user has selected to view recipe they are take to a page containing the full information of the chosen cocktail if the user is logged in they will also have the option to add the drink to their favourites or if it is already present in their favourited list to remove it from favourties.

Create Cocktail
	registered users that are logged in will be able to create recipes to be added to the database through this page they are asked to enter
	cocktail name*
	Cocktail descrition*
	Method*
	image url*
	the glass to serve it in
	and ingredients from 1 to 13 from a drop down or predictive text box and the measure
asterix items are require and from the ingredients  1 and 2 are required before being able to upload.

Edit Recipe

Once a user has created a recipe they then have the ablity to edit their creations if their username matches the created by field in the database. 

A identical form to the creation page and is populated with the information that was previously entered. Once they have updated these fielfds they are able to click the subit button and the recipe will be updated in the database.

Delete recipe
	User have the option to remove cocktails they have create by clicking the delete button available to them again if their username matches the created_by field in the database,

Once clicked the cocktail is removed from the database and this cannot be undone the cocktail will be removed from their profile and from the database by which removing access for all other users.

Search fucntion

Users are able to search the database on the drinks list page. They are able to search by keywords for category, drink name and ingredient this is currently a standard mongodb or search function uing text indexs meaning for each word entered it will produce more results. In future development I would change this to a and search.


Technologies Used
GitPod online IDE
GitHub - Remote repository for all project code with git version control.
Front-End Technologies
HTML - The fundamental code structure for all webpages.
 CSS -  Custom CSS was used for this project to alter the default CSS of the bootstrap framework.
jQuery 3.3.1 - Javascript framework used to implement custom code and initialize Materialize functions.
Bootstrap 5 - Primary visual framework for this project.
Back-End Technologies
Flask
Flask 1.0.2 - A templating microframework used to dynamically build the pages in this project.
Jinja 2.10 - HTTP templating language for Python.
Werkzeug 0.14 - Werkzeug is a comprehensive WSGI web application library. Installed as a dependency of Flask, it provides password hashing and checking for this project.
Heroku
Heroku - Hosts the deployed version of this project.
Python
Python 3.7.3 - Python is an interpreted, high-level, general-purpose programming language and is the language used for all backend functions of this project.
MongoDB Atlas - MongoDB Atlas is the online host for remote MongoDB's NoSQL document-oriented databases.
PyMongo 3.8.0 - PyMongo is a Python distribution containing tools for working with MongoDB.
Python dotenv - Reads the values of the environmental variables that are set in the project's .env file.

Testing
	Due to time constraints, I was  unable to design and implement automatic Unit-testing for this project, and so developer and user manual testing was completed instead. 

HTML
Passing the HTML from all templates and base into the W3C Markup Validator generates numerous errors, but these are expected as the validator is unable to understand the Jinja2 templating that builds most aspects of the page. For the HTML that does not involve Jinja2, no errors have been found.
CSS
The CSS for the project has been generated by the Sass CSS extension language. Passing the generated CSS through the W3C CSS Validation Service shows that there are no errors. A number of warnings are flagged, but these relate to MS-Grid vendor prefixes and can be safely ignored.
Javascript
All Javascript was passes throught the Esprima Syntax Validator and was found to be syntactically valid.
Python
All Python code was passed through the PEP8 Online validator and is fully PEP8 compliant.
Compatibility
The project was tested to ensure full usability across the following browsers and their mobile equivalents (where applicable):
Chrome v.74
Edge v.18
Firefox v.67
Safari v.12
Opera v.56
Internet Explorer v.11
Deployment
Local Deployment

Sign up for a free account on MongoDB and create a new Database . The Collections in that database should be as follows:
	
	users collection containing:
	_id: <ObjectId>
	username: <string>
	password: <string>
	favourite: <array>

	ingredients collection containg:
	_id:608e743eca13bb1045e62469
1. idIngredient:<string>
2. strIngredient:<string>
3. strDescription:<string>
4. strType:<string>
5. strAlcohol:<string>
6. strABV:<string>

	catergories collection containg:
	_id:60896850bf21439a00c79584
1. category_name:"Vodka"
	drinks collection containing 
	_id:60912ebbd7e1a43db1e85e61
1. idDrink:"11129"
2. strDrink:"Boston Sour"
3. strDrinkAlternate:null
4. strTags:null
5. strVideo:null
6. strCategory:"Ordinary Drink"
7. strIBA:null
8. strAlcoholic:"Alcoholic"
9. strGlass:"Whiskey sour glass"
10. strInstructions:"Shake juice of lemon, powdered sugar, blended whiskey, and egg white w..."
11. strInstructionsES:null
12. strInstructionsDE:"Den Saft von Zitrone, Puderzucker, gemischtem Whiskey und Eiweiß mit z..."
13. strInstructionsFR:null
14. strInstructionsIT:"Shakerare il succo di limone, lo zucchero a velo, il whisky miscelato ..."
15. strInstructionsZH-HANS:null
16. strInstructionsZH-HANT:null
17. strDrinkThumb:"https://www.thecocktaildb.com/images/media/drink/kxlgbi1504366100.jpg"
18. strIngredient1:"Blended whiskey"
19. strIngredient2:"Lemon"
20. strIngredient3:"Powdered sugar"
21. strIngredient4:"Egg white"
22. strIngredient5:"Lemon"
23. strIngredient6:"Cherry"
24. strIngredient7:null
25. strIngredient8:null
26. strIngredient9:null
27. strIngredient10:null
28. strIngredient11:null
29. strIngredient12:null
30. strIngredient13:null
31. strIngredient14:null
32. strIngredient15:null
33. strMeasure1:"2 oz "
34. strMeasure2:"Juice of 1/2 "
35. strMeasure3:"1 tsp "
36. strMeasure4:"1 "
37. strMeasure5:"1 slice "
38. strMeasure6:"1 "
39. strMeasure7:null
40. strMeasure8:null
41. strMeasure9:null
42. strMeasure10:null
43. strMeasure11:null
44. strMeasure12:null
45. strMeasure13:null
46. strMeasure14:null
47. strMeasure15:null
48. strImageSource:null
49. strImageAttribution:null
50. strCreativeCommonsConfirmed:"No"
51. dateModified:"2017-09-02 16:28:20"
52. category_name:"Whisky"
53. created_by:"admin"

At the terminal prompt, type flask run. Flask should now start running a development server from 'http://127.0.0.1:5000'. Copy and paste this address to your browser and you should now see the project running.
Remote Deployment
To implement this project on Heroku, the following must be completed:
1. Create a requirements.txt file so Heroku can install the required dependencies to run the app.
sudo pip3 freeze --local > requirements.txt
My file can be found here.
2. Create a Procfile to tell Heroku what type of application is being deployed, and how to run it.
echo web: python run.py > Procfile
My file can be found here.
3. Sign up for or log into your Heroku account, create your project app, and click the Deploy tab. Select Connect GitHub as the Deployment Method, and select Enable Automatic Deployment.
4. In the Heroku Settings tab, click on the Reveal Config Vars button to configure environmental variables as follows:
IP : 0.0.0.0
PORT : 8080
MONGO_URI : <link to your Mongo DB>
SECRET_KEY : <your own secret key>
5. The app will now be deployed and built by Heroku and will be ready to run.




Creating the Project
This project used the Code Institute's student template. A new repository named ms3-pickyourpoison was created which included all branches from the template. The project was developed using the IDE GitPod. Version control software Git was used to commit and push the code to GitHub where it was stored. The following commands were used for this:
git add filename/directory - This command adds files/directories to the staging area to be committed.
git commit -m "message here" - This command commits files/directories to the repository. Commit messages should clearly explain the update being committed.
git push - This command pushes all committed updates/changes into the GitHub repository.
Deploying to Heroku
Heroku needs some files to be setup so that it knows what apps and dependencies are needed to run the app.
use the command "pip3 freeze --local > requirements.txt".
use the command "echo web: python app.py > Procfile" (ensuring you enter a capital P).
Add, commit and push.
Create Heroku App:
Create an account or login to Heroku.
Click on the New button on the top right of your dashboard.
Select Create new app.
Enter your new unique app name.
Choose your region.
Select Create app.
Connect to GitHub Repository:
On your new app's page, navigate to the Deploy tab.
Under Deployment method, select GitHub.
Under Connect to GitHub (and making sure your GitHub profile is displayed), enter the name of your repository and click Search.
Once your repo has been found, click Connect.
Set Environment Variables:
Navigate to your app's Settings tab.
Under Config Vars, click Reveal Config Vars.
You'll need to add the following key:value items;
key: IP, value: 0.0.0.0
key: PORT, value: 5000
key: MONGO_DBNAME, value: (database name you want to connect to)
key: MONGO_URI, value: (accessed by following the steps below)
Login to MongoDB.
Under Data Storage, click Clusters.
Click Connect on the cluster you want.
Click Connect your application.
Copy the link there, replacing < password > with your own one for the database access page, and the database name with the collection/database you want to collect to.
key: SECRET_KEY, value: (your own secret key)
custom and random sequence of characters required for maintaining security.
generated from RandomKeygen for example.
Automatic Deployment:
Navigate back to your app's Deployment tab.
Under Automatic deploys, select the branch you wish to deploy from.
Click Enable Automatic Deploys.
Deploying Locally
Please note that the project will not run locally without a new env.py python file being created which contains the following with their corresponding values: IP, PORT, MONGO_DBNAME, MONGO_URI, SECRET_KEY. For security reasons, these details are not included in this repository.
In order to make a clone, follow these steps:
Log into GitHub.
Navigate to the Repositories tab.
Choose the desired repository.
Above the list of files, click on the Code drop-down menu.
Copy the clone URL under the HTTPS tab.
Open a terminal window in your IDE of choice.
Change the working directory to whichever location you want the cloned directory to be in.
Type git clone and then paste the URL that you copied earlier.
Press enter to create the clone.
In your IDE of choice, type pip install -r requirements.txt in order to install all required packages for project.

Credits
 content:
	I scraped off the recipes and images from https://www.thecocktaildb.com/api.php to populate the database
    favicon is from https://www.favicon-generator.org/search/---/Alcohol
    missing picture image from: https://www.nationalpetregister.org/assets/img/no-photo.jpg
code snippets:
	pagination adapted from:
https://gist.github.com/mozillazg/69fb40067ae6d80386e10e105e6803c9
Acknowledgements:
	My tutor chris quinn
