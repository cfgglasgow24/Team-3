from flask import Flask, render_template, request

from questions import Question

app = Flask(__name__)

@app.route("/")
def index():
    letter = Question.get_random_letter()
    question = Question(letter)
    return render_template("learn.html", question=question)

@app.route("/check_answer", methods=["POST"])
def check_answer():
    print(request.form)
    answer_selected = request.form["answer"]
    question_letter = request.form["question"]
    question = Question(question_letter)
    if int(answer_selected) == int(question.button_number):
        message = "Correct!"
    else:
        message = "Wrong!"

    letter = Question.get_random_letter()
    question = Question(letter)

    return render_template("learn.html", question=question, message=message)

if __name__ == "__main__":
    app.run(debug=True)