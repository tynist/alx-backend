#!/usr/bin/env python3
"""Get locale from request"""

from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)

# Instantiate Babel object
babel = Babel(app)


# Config class for Flask app
class Config:
    # Available languages
    LANGUAGES = ["en", "fr"]

    # Babel configuration
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    # Get the best match of supported languages
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(debug=True)
