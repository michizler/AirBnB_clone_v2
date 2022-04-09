#!/usr/bin/python3
"""
starts a Flask web application:

must be listening on 0.0.0.0, port 5000
Routes:
/: display “Hello HBNB!”
/hbnb: display “HBNB”
/c/<text>: display “C ”, followed by the value of
the text variable (replace underscore _ symbols with a space )
/python/(<text>): display “Python ”, followed by the value of
the text variable (replace underscore _ symbols with a space )
The default value of text is “is cool”
"""

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_hbnb():
    """Display 'Hello HBNB!'"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """Display 'HBNB'"""
    return 'HBNB'


@app.route('/c/<text>')
def c(text):
    """Display 'C ' followed by the value of
    the text variable (replace underscore _ symbols with a space )"""
    return 'C ' + text.replace('_', ' ')


@app.route('/python/')
@app.route('/python/<text>')
def python(text='is cool'):
    """Display 'Python ' followed by the value of
    the text variable (replace underscore _ symbols with a space )"""
    return 'Python ' + text.replace('_', ' ')
