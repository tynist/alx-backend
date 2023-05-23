#!/usr/bin/env python3
"""
Use user locale
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """
    Configuration class for the Flask app
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


def get_user(login_as):
    """
    Retrieve a user based on the login_as parameter.
    """
    try:
        return users.get(int(login_as))
    except Exception:
        return


@app.before_request
def before_request():
    """
    Execute before each request to set the global user
    """
    g.user = get_user(request.args.get("login_as"))


@babel.localeselector
def get_locale():
    """
    Get the locale to use for translations.
    """
    locale = request.args.get("locale")
    if locale and locale in app.config["LANGUAGES"]:
        return locale

    user = request.args.get("login_as")
    if user:
        user_locale = users.get(int(user)).get("locale")
        if user_locale and user_locale in app.config["LANGUAGES"]:
            return user_locale

    headers = request.headers.get("Accept-Language")
    if headers:
        langs = [lang.strip() for lang in headers.split(",")]
        for lang in langs:
            if lang in app.config["LANGUAGES"]:
                return lang

    return app.config["BABEL_DEFAULT_LOCALE"]


@app.route("/", methods=["GET"], strict_slashes=False)
def hello():
    """
    Render the index template with the appropriate messages.
    """
    return render_template("6-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
