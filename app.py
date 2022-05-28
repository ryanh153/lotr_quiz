import numpy as np
from flask import Flask, render_template, request

from questions import questions

app = Flask(__name__)


@app.route('/')
def base_question():
    print('in base')
    ii = np.random.randint(0, len(questions))
    print(f'Picked index {ii}')
    question = questions[ii]
    return render_template('base_question.html', question=question)


@app.route('/with_options', methods=['POST'])
def with_options():
    print('in with options')
    ii = int(request.form['question_index'])
    return render_template('with_options.html', question=questions[ii])


@app.route('/with_answer', methods=['POST'])
def with_answer():
    print('in with answer')
    ii = int(request.form['question_index'])
    return render_template('with_answer.html', question=questions[ii])


if __name__ == "__main__":
    app.run()
