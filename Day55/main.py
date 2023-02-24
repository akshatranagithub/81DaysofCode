from flask import Flask
import random

app = Flask(__name__)


@app.route("/")
def home():
    return '<h1><strong>Guess a number between 0 and 9<strong></h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"></img>'


@app.route("/<int:guess_number>")
def guess(guess_number):
    if guess_number < number:
        return "<h1 style='color:red'><strong>Too Low, try again!<strong></h1>" \
               '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"></img>'
    elif guess_number > number:
        return "<h1 style='color:voilet'><strong>Too High, try again!<strong></h1>" \
               '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"></img>'
    else:
        return "<h1 style='color:green'><strong>You found me!!!<strong></h1>" \
               '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"></img>'


if __name__ == '__main__':
    number = random.randint(0, 9)
    app.run(debug=True)
