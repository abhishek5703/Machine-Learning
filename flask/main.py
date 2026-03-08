'''
Integrating Flask with HTML means showing HTML pages instead of plain text responses. Flask uses the template engine Jinja to render HTML files.
'''
# The HTML templates are present in the templates folder
# Import Flask and render_template
from flask import Flask, render_template

# Create Flask app
app = Flask(__name__)

# Home route
@app.route("/")
def home():
    # render_template loads HTML file from templates folder
    return render_template("index.html")

# About route
@app.route("/about")
def about():
    return render_template("about.html")

# Run the server
if __name__ == "__main__":
    app.run(debug=True)