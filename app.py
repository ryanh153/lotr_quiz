import numpy as np
from flask import Flask, render_template, request, session
import jsonpickle

from data_objects.questions import questions
from data_objects.player import Player

app = Flask(__name__)
app.secret_key = 'any_random_string'


@app.route('/')
def index():
    print('home')
    player = Player()
    store_data(player)
    return render_template('index.html')


@app.route('/base_question')
def base_question():
    print('in base')
    ii = np.random.randint(0, len(questions))
    print(f'Picked index {ii}')
    player = retrieve_data()
    question = questions[ii]
    return render_template('base_question.html', question=question, player=player)


@app.route('/with_options', methods=['POST'])
def with_options():
    print('in with options')
    player = retrieve_data()
    ii = int(request.form['question_index'])
    return render_template('with_options.html', question=questions[ii], player=player)


@app.route('/with_answer', methods=['POST'])
def with_answer():
    print('in with answer')
    player = retrieve_data()
    ii = int(request.form['question_index'])
    return render_template('with_answer.html', question=questions[ii], player=player)


@app.route('/increment_counter', methods=['POST'])
def increment_counter():
    print('in incrementer')
    ii = int(request.form['question_index'])
    player = retrieve_data()
    player.correct_answer()
    store_data(player)
    return render_template('with_answer.html', question=questions[ii], player=player)


@app.route('/reset_counter', methods=['POST'])
def reset_counter():
    print('in streak reset')
    ii = int(request.form['question_index'])
    player = retrieve_data()
    player.incorrect_answer()
    store_data(player)
    return render_template('with_answer.html', question=questions[ii], player=player)


def store_data(player: Player):
    session['player'] = jsonpickle.encode(player)


def retrieve_data() -> Player:
    return jsonpickle.decode(session['player'])


if __name__ == "__main__":
    app.run()
