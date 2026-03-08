# Import required modules
# We use the GET and the POST request to get the info and post the info
from flask import Flask, render_template, request

# Create Flask application
app = Flask(__name__)

# Route that supports both GET and POST
@app.route("/", methods=["GET", "POST"])
def home():

    # POST request (when form is submitted)
    if request.method == "POST":
        name = request.form.get("username")
        return f"Hello {name}, your form was submitted!"

    # GET request (when page loads normally)
    return render_template("form.html")


# Run Flask server
if __name__ == "__main__":
    app.run(debug=True)