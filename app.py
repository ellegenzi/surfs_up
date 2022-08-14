# Import Flask dependency
from flask import Flask

# Create a New Flask App Instance
# We're now ready to create a new Flask app instance. "Instance" is a general term in programming to refer to a singular version of something.
# Add the following to your code to create a new Flask instance called app:

app = Flask(__name__)

# IMPORTANT: You probably noticed the __name__ variable inside of the Flask() function. Let's pause for a second and identify what's going on here.
# This __name__ variable denotes the name of the current function. You can use the __name__ variable to determine if your code is being run from the
# command line or if it has been imported into another piece of code. Variables with underscores before and after them are called magic methods in Python.

# Create Flask Routes
# Our Flask app has been created—let's create our first route!

# First, we need to define the starting point, also known as the root. To do this, we'll use the function @app.route('/'). Add this to your code now.

@app.route('/')

# NOTE: Notice the forward slash inside of the app.route? This denotes that we want to put our data at the root of our routes. The forward slash is
# commonly known as the highest level of hierarchy in any computer system.

# Next, create a function called hello_world(). Whenever you make a route in Flask, you put the code you want in that specific route below @app.route(). Here's what it will look like:

@app.route('/')
def hello_world():
    return 'Hello world'

# Run a Flask App
# The process of running a Flask app is a bit different from how we've run Python files. To run the app, we're first going to need to use the command line to navigate to the folder
# where we've saved our code. You should save this code in the same folder you've used in the rest of this module.

# Once you've ensured that your code is saved in the proper directory, then run the following command in Anaconda Powershell.
# This command sets the FLASK_APP environment variable to the name of our Flask file, app.py.

# NOTE: Environment variables are essentially dynamic variables in your computer. They are used to modify the way a certain aspect of the computer operates.
# For our FLASK_APP environment variable, we want to modify the path that will run our app.py file so that we can run our file.

# set FLASK_APP=app.py

# Now let's run our Flask app. To do this, type the following command in your command line and press Enter:

# flask run

# When you run this command, you'll notice a line that says "Running on" followed by an address. This should be your localhost address and a port number.

# IMPORTANT: A port number is essentially the endpoint of a given program or service. Any Flask application you create can have whatever port number you would like,
# but the most common is 5000.

# Copy and paste your localhost address into your web browser. Generally, a localhost will look something like this, for context.

# localhost:5000