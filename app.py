import logging

from flask import Flask, render_template

from data_objects.player import Player
from utils.data_storage import store_player_data
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
    store_player_data(player)
    return render_template('index.html')


@app.route('/base_question')
@render_wrapper(new_question=True)
def base_question(page_data):
    logger.debug('in base')
    return render_template('base_question.html', page_data=page_data)


@app.route('/with_options', methods=['POST'])
@render_wrapper()
def with_options(page_data):
    logger.debug('in with options')
    return render_template('with_options.html', page_data=page_data)


@app.route('/with_answer', methods=['POST'])
@render_wrapper()
def with_answer(page_data):
    logger.debug('in with answer')
    return render_template('with_answer.html', page_data=page_data)


@app.route('/increment_counter', methods=['POST'])
@render_wrapper()
def increment_counter(page_data):
    logger.debug('in incrementer')
    page_data.player.correct_answer()
    return base_question()


@app.route('/reset_counter', methods=['POST'])
@render_wrapper()
def reset_counter(page_data):
    logger.debug('in streak reset')
    page_data.player.incorrect_answer()
    return base_question()


if __name__ == "__main__":
    app.run(debug=False)
