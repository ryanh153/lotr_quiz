import numpy as np
from flask import Flask, render_template, request

from data_objects.questions import questions
from data_objects.player import player

app = Flask(__name__)


@app.route('/')
def base_question():
    print('in base')
    ii = np.random.randint(0, len(questions))
    print(f'Picked index {ii}')
    question = questions[ii]
    return render_template('base_question.html', question=question, streak=player.streak)


@app.route('/with_options', methods=['POST'])
def with_options():
    print('in with options')
    ii = int(request.form['question_index'])
    return render_template('with_options.html', question=questions[ii], streak=player.streak)


@app.route('/with_answer', methods=['POST'])
def with_answer():
    print('in with answer')
    ii = int(request.form['question_index'])
    return render_template('with_answer.html', question=questions[ii], streak=player.streak)


@app.route('/increment_counter', methods=['POST'])
def increment_counter():
    print('in incrementer')
    ii = int(request.form['question_index'])
    player.streak += 1
    return render_template('with_answer.html', question=questions[ii], streak=player.streak)


@app.route('/reset_counter', methods=['POST'])
def reset_counter():
    print('in streak reset')
    ii = int(request.form['question_index'])
    player.streak = 0
    return render_template('with_answer.html', question=questions[ii], streak=player.streak)


if __name__ == "__main__":
    app.run()
