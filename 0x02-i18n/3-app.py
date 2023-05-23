#!/usr/bin/env python3
"""
Parametrize templates
"""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)

# Instantiate Babel object
babel = Babel(app)


# Config class for Flask app
class Config:
    """
    Configuration class for the Flask app.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    # Determine the best match with the supported languages
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """
    Render the index template with parametrized messages.
    """
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(debug=True)
