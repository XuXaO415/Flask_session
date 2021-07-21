from flask import Flask, request, render_template, flash, redirect, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey
# from surveys import personality_survey as survey
# from survey import surveys

choose_survey = 'choose_survey'
responses = "responses"
# responses = []

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)


@app.route('/')
def show_surveys():
    return render_template('start.html')


@app.route("/start", methods=["POST"])
def start_survey():
    """Clear the session of responses."""

    session[responses] = []
    return redirect("/questions/0")


@app.route("/answer", methods=["POST"])
def handle_question():
    """Save response and redirect to next question."""

    # get the response choice
    choice = request.form['answer']

    # add this response to the session
    responses = session['responses']
    responses.append(choice)
    session['responses'] = responses

    if (len(responses) == len(survey.questions)):
        # They've answered all the questions! Thank them.
        return redirect("/thanks")

    else:
        return redirect(f"/questions/{len(responses)}")


@app.route("/questions/<int:qid>")
def show_question(qid):
    """Display current question."""
    responses = session.get('responses')

    if (responses is None):
        # trying to access question page too soon
        return redirect("/")

    if (len(responses) == len(survey.questions)):
        # They've answered all the questions! Thank them.
        return redirect("/thanks")

    if (len(responses) != qid):
        # Trying to access questions out of order.
        # flash(f"Invalid question id: {qid}.")
        flash(f"You can't do that!")
        return redirect(f"/questions/{len(responses)}")

    question = survey.questions[qid]
    return render_template(
        "questions.html", question_num=qid, question=question)


# @app.route("/surveys")
# def new_survey():
#     return render_template('personality.html')


@app.route("/thanks")
def thanks():
    """Survey complete. Show completion page."""
    return render_template("thanks.html")

##########
# Made a change for test purpose
##########
