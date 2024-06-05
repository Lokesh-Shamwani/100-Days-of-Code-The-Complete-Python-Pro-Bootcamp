from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper_function():
        return "<b>" + function() + "</b>"

    return wrapper_function



def make_emphasis(function):
    def wrapper_function():
        return "<em>" + function() + "</em>"

    return wrapper_function


def make_underlined(function):
    def wrapper_function():
        return "<u>" + function() + "</u>"

    return wrapper_function


@app.route("/")  
def hello_world():
    return (
        "<h1 style='text-align: center'>hello world qwerty!</h1>"
        "<p>This ia a paragraph </p>"
    )


@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def say_bye():
    return "Bye"


# @app.route("/<name>")
# def greet(name):
#     return f"Hello there {name}!"


@app.route("/<path:name>/<int:number>")  # for using slash in variable "name"
def greet(name, number):
    return f"Hello there {name}, you're {number} years old!"


if __name__ == "__main__":
    app.run(debug=True)
