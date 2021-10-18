import os
import json
# We are impoting Flask class from flask package
from flask import Flask, render_template

#  This is an instance of using this class and storing it in a variable called app.
#  The first arg is the name of the application's module - our package.
#  since we are just using a single module we can use __name__ which is a built-in python variable.
app = Flask(__name__)



#  we use route decorator to tell Flask what URL should trigger the function that follows.
#  with "/" we try to browse to the root directory.
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    data =[]
    with open("data/company.json", "r") as json_data:
        data= json.load(json_data)
    return render_template("about.html", page_title="About", company = data)    

@app.route("/contact")
def contact():
    return render_template("contact.html", page_title="Contact")   


@app.route("/career")
def career():
    return render_template("career.html", page_title="Careers") 



# The name "__main__" is the name of default module in Python.
# This is the first one that we run, so if it has not been imported, it will be run directly.
# We get the IP environment if it exist and set a default if not found.
#  5000 is common port used by Flask.
# We should never have the debug ==true in a production app or when we submit projects for assessmnet.
# This can allow arbitary code to be run and then is a security flaw. we can have it true only to test 
#  the app or to debug.

if __name__ == "__main__":
    app.run(
        host = os.environ.get("IP", "0.0.0.0"),
        port = int(os.environ.get("PORT", "5000")),
        debug = True)
