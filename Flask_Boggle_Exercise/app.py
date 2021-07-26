from flask import Flask, request, render_template, session, jsonify
from boggle import Boggle

boggle_game = Boggle()

app = Flask(__name__)
app.config["SECRET_KEY"] = "SHHHHHHHHHHH SEEKRIT"


@app.route("/")
def show_homepage():
    """Shows homepage with board"""
    board = boggle_game.make_board()
    session["board"] = board
    return render_template("index.html", board=board)
