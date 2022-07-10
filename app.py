import logging

from flask import Flask, render_template, request

from data_objects.player import Player
from data_objects.questions import questions
from utils.data_storage import retrieve_data, store_data
from utils.render_template_helpers import render_wrapper

app = Flask(__name__)
app.secret_key = 'any_random_string'
LOG_FORMAT = '%(asctime)s - %(filename)s - %(lineno)d: %(message)s'
logging.basicConfig(format=LOG_FORMAT, level=logging.DEBUG)
logger = logging.getLogger(__name__)


@app.route('/')
def index():
    logger.debug('home')
    player = Player()
    store_data(player)
    return render_template('index.html')


@app.route('/base_question')
@render_wrapper
def base_question(question, player):
    logger.debug('in base')
    return render_template('base_question.html', question=question, player=player)


@app.route('/with_options', methods=['POST'])
def with_options():
    logger.debug('in with options')
    player = retrieve_data()
    ii = int(request.form['question_index'])
    return render_template('with_options.html', question=questions[ii], player=player)


@app.route('/with_answer', methods=['POST'])
def with_answer():
    logger.debug('in with answer')
    player = retrieve_data()
    ii = int(request.form['question_index'])
    return render_template('with_answer.html', question=questions[ii], player=player)


@app.route('/increment_counter', methods=['POST'])
def increment_counter():
    logger.debug('in incrementer')
    ii = int(request.form['question_index'])
    player = retrieve_data()
    player.correct_answer()
    store_data(player)
    return render_template('with_answer.html', question=questions[ii], player=player)


@app.route('/reset_counter', methods=['POST'])
def reset_counter():
    logger.debug('in streak reset')
    ii = int(request.form['question_index'])
    player = retrieve_data()
    player.incorrect_answer()
    store_data(player)
    return render_template('with_answer.html', question=questions[ii], player=player)


if __name__ == "__main__":
    app.run(debug=True)
