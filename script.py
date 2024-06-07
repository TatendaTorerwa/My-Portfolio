#!/usr/bin/env python3

from flask import Flask, render_template

app = Flask(__name__)
"""Variable to storethe flask applicaton..creating a flask instance."""

@app.route('/')
def home():
    return render_template("home.html")
@app.route('/about/')
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)

