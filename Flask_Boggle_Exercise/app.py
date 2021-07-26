from flask import Flask, request, render_template, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from boggle import Boggle

boggle_game = Boggle()

app = Flask(__name__)
app.config["SECRET_KEY"] = "SHHHHHHHHHHH SEEKRIT"
debug = DebugToolbarExtension(app)


@app.route("/")
def show_homepage():
    """Shows homepage with board"""
    board = boggle_game.make_board()
    session["board"] = board
    return render_template("index.html", board=board)

# # Step 3 --checking for a valid word


# @app.route("/check_for_valid_word")
# def check_for_valid_word():

#     # Step 4 --posting a score


# @app.route("/post_score", methods=["POST"])
