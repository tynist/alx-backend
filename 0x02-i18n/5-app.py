#!/usr/bin/env python3
"""
Mock logging in
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """
    Configuration class for the Flask app.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(user_id):
    """
    Retrieve a user based on the login_as parameter.
    """
    return users.get(user_id)


@app.before_request
def before_request():
    """
    Execute before each request to set the global user.
    """
    login_as = request.args.get("login_as")
    if login_as:
        user_id = int(login_as)
        g.user = get_user(user_id)
    else:
        g.user = None


@babel.localeselector
def get_locale():
    """
    Get the locale to use for translations.
    """
    if g.user and g.user["locale"] in app.config["LANGUAGES"]:
        return g.user["locale"]
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def index():
    """
    Render d index template with d right messages & user login status
    """
    if g.user:
        message = gettext("You are logged in as %(username)s.") % {
            "username": g.user["name"]
        }
    else:
        message = gettext("You are not logged in.")
    return render_template("5-index.html", message=message)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
