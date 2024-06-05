from flask import Flask
import random

random_number = random.randint(0, 9)
print(random_number)

app = Flask(__name__)


@app.route("/")
def home():
    return (
        "<h1> Guess a number between 0 and 9 </h1>"
        "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' alt='an gif here'> "
    )


@app.route("/<int:url_number>")
def show_feedback(url_number):
    if random_number == url_number:
        return '<h1 style="color:green">You found me! </h1>' \
        "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif' alt='an gif here'> "
    elif url_number > random_number:
        return '<h1 style="color:purple">Too high, try again!</h1>' \
        "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif' alt='an gif here'> "
    else:
        return '<h1 style="color:red">Too low, try again!</h1>' \
        "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif' alt='an gif here'> "


if __name__ == "__main__":
    app.run(debug=True)
    
