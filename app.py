from flask import Flask, render_template, request, redirect, url_for
from models import Quiz, Question

app = Flask(__name__)

quiz_obj = Quiz()


@app.route('/')
def start_quiz():
    return render_template('home.html')


@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if quiz_obj.is_finished():
        return redirect(url_for('result'))

    question = quiz_obj.get_current_question()

    if request.method == 'POST':
        if 'answer' in request.form:
            answer = request.form['answer']
            quiz_obj.check_answer(answer)
            quiz_obj.next_question()
            return redirect(url_for('quiz'))
        else:
            return render_template('quiz.html', question=question, error="Please select an answer")

    return render_template('quiz.html', question=question)



@app.route('/result')
def result():
    score = quiz_obj.score

    render_tmp = render_template('result.html', score=score)

    quiz_obj.reset()

    return render_tmp


if __name__ == '__main__':
    app.run(debug=True)
