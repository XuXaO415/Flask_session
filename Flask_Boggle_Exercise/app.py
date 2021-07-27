from flask import Flask, request, render_template, session, jsonify, flash
from flask_debugtoolbar import DebugToolbarExtension
from boggle import Boggle

boggle_game = Boggle()
# board = "board"
# word = "words.txt"


app = Flask(__name__)
app.config["SECRET_KEY"] = "SHHHHHHHHHHH SEEKRIT"
# app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
debug = DebugToolbarExtension(app)


@app.route("/")
def show_homepage():
    """Shows homepage with board"""
    board = boggle_game.make_board()
    session["board"] = board
    highscore = session.get("score", 0)
    # flash("Are you ready to play?")
    return render_template("base.html", board=board, highscore=highscore)

# Step 3 --checking for a valid word


@app.route("/check_for_valid_word")
# Make sure that the word is valid on the board using the check_valid_word function from the boggle.py file
def check_for_valid_word():
    # On the server, take the form value and check if it is a valid word in the dictionary using the words variable in your app.py.
    word = request.args["word"]
    board = session["board"]
    # Next, make sure that the word is valid on the board using the check_valid_word function from the boggle.py file.
    res = boggle_game.check_valid_word(word, board)

# Since you made an AJAX request to your server, you will need to respond with JSON using the jsonify function from Flask.
# Send a JSON response which contains either a dictionary of {“result”: “ok”}, {“result”: “not-on-board”}, or {“result”: “not-a-word”}, so the front-end can provide slightly different messages depending if the word is valid or not.
    # return jsonify({resp: "result"})
    return jsonify({'result': res})

    #  Step 4 --posting a score

#  @app.route("")
