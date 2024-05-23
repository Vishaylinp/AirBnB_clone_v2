#!/usr/bin/python3
"""Flask web app"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """return Hello"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """return hbnb"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """"Display text
    Arg: text: text
    """
    return "C {}".format(text.replace("_", " "))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    """Display text
    Arg: text: text
    """
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def is_num(n):
    """Display number
    Arg: n : number
    """
    if isinstance(n, int):
        return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def numb_template(n=None):
    """Display number in html
    Arg: n : number
    """
    if isinstance(n, int):
        return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def even_or_odd_num(n=None):
    """Display number in html even or odd
    Arg: n : number
    """
    if isinstance(n, int):
        if n % 2:
            r = "odd"
        else:
            r = "even"
        return render_template("6-number_odd_or_even.html", n=n, r=r)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
