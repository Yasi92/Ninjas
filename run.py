import os
# We are impoting Flask class from flask package
from flask import flask

#  This is an instance of using this class and storing it in a variable called app.
#  The first arg is the name of the application's module - our package.
#  since we are just using a single module we can use __name__ which is a built-in python variable.
app = Flask(__name__)



#  we use route decorator to tell Flask what URL should trigger the function that follows.
#  with "/" we try to browse to the root directory.
@app.route("/")
def index():
    return "Hello, World"




# The name "__main__" is the name of default module in Python.
# This is the first one that we run, so if it has not been imported, it will be run directly.
if __name__ == "__main__":
    app.run(
        # We get the
         IP environment if it exist and set a default if not found.
        #  5000 is common port used by Flask.
        # 
        host = os.environ.get("IP", "0.0.0.0"),
        port = int(os.environ.get("PORT", "5000")),
        debug = True
    )
