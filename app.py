import logging

from flask import Flask, render_template

from data_objects.player import Player
from data_objects.questions import load_questions
from utils.data_storage import store_data
from utils.render_template_helpers import render_wrapper

app = Flask(__name__)
app.secret_key = 'any_random_string'

LOG_FORMAT = '%(asctime)s - %(filename)s - %(lineno)d: %(message)s'
logging.basicConfig(format=LOG_FORMAT, level=logging.DEBUG)
logger = logging.getLogger(__name__)

questions = load_questions()


@app.route('/')
def index():
    logger.debug('home')
    player = Player()
    store_data(player)
    return render_template('index.html')


@app.route('/base_question')
@render_wrapper(questions, new_question=True)
def base_question(question, player):
    logger.debug('in base')
    return render_template('base_question.html', question=question, player=player)


@app.route('/with_options', methods=['POST'])
@render_wrapper(questions)
def with_options(question, player):
    logger.debug('in with options')
    return render_template('with_options.html', question=question, player=player)


@app.route('/with_answer', methods=['POST'])
@render_wrapper(questions)
def with_answer(question, player):
    logger.debug('in with answer')
    return render_template('with_answer.html', question=question, player=player)


@app.route('/increment_counter', methods=['POST'])
@render_wrapper(questions)
def increment_counter(question, player):
    logger.debug('in incrementer')
    player.correct_answer()
    return render_template('with_answer.html', question=question, player=player)


@app.route('/reset_counter', methods=['POST'])
@render_wrapper(questions)
def reset_counter(question, player):
    logger.debug('in streak reset')
    player.incorrect_answer()
    return render_template('with_answer.html', question=question, player=player)


if __name__ == "__main__":
    app.run(debug=False)
