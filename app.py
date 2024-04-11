from flask import Flask, render_template, request

from questions import Question

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/templates/learn.html")
def learn():
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
        message = f"Correct! Well done! Explanation: {question.explanation}"

        letter = Question.get_random_letter()
        question = Question(letter)
    else:
        message = "Try again!"

    return render_template("learn.html", question=question, message=message)

if __name__ == "__main__":
    app.run(debug=True)