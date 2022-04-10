#!/usr/bin/python3
"""
Starts a Flask web application

must be listening on 0.0.0.0, port 5000

Routes:
/: display "Hello HBNB!"
/hbnb: display "HBNB"
/c/<text>: display "C ", followed by the value of the text
variable (replace underscore _ symbols with a space )

/python/(<text>): display "Python ", followed by the value of the text
 variable (replace underscore _ symbols with a space )
The default value of text is "is cool"
/number/<n>: display "n is a number" only if n is an integer
/number_template/<n>: display a HTML page only if n is an integer:
H1 tag: "Number: n" inside the tag BODY
"""


from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_hbnb():
    """
    Display Hello HBNB!
    """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """Display HBNB!"""
    return 'HBNB'


@app.route('/c/<text>')
def c_text(text):
    """Display C is ..."""
    return 'C ' + text.replace('_', ' ')


@app.route('/python/<text>')
def python_text(text='is cool'):
    """Display python is..."""
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int n>')
def number(n):
    """Display n is a number"""
    return str(n) + ' is a number'


@app.route('/number_template/<int n>')
def number_template(n):
    """Display an html page only if n is a number"""
    return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int n>', strict_slashes=False)
def number_odd_or_even(n):
    """Displays an HTML page only if <n> is an integer.
    States whether <n> is odd or even in the body."""
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
