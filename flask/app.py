# Import the Flask class from the flask package
# Flask is used to create the web application
from flask import Flask


# Create an instance (object) of the Flask class
# __name__ tells Flask where the application is located
app = Flask(__name__)


# The route decorator tells Flask what URL should trigger the function below
# "/" means the homepage of the website
@app.route("/")
def home():
    # This function runs when someone visits http://127.0.0.1:5000/
    
    # The return value is sent back to the browser
    return "Hello Abhishek! Your Flask app is running "


# Another route example
# If a user visits http://127.0.0.1:5000/about
@app.route("/about")
def about():
    # This function will execute
    return "This is the About Page"


# This condition ensures the server runs only when this file is executed directly
# and not when it is imported in another Python file
if __name__ == "__main__":
    
    # app.run() starts the Flask development server
    
    # debug=True means:
    # 1. The server will automatically reload when you change the code
    # 2. It shows detailed error messages in the browser
    app.run(debug=True)