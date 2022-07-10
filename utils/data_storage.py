import jsonpickle
from flask import session


def store_player_data(player):
    session['player'] = jsonpickle.encode(player)


def retrieve_player_data():
    return jsonpickle.decode(session['player'])


def store_index_data(question_index, image_index):
    session['question_index'] = jsonpickle.encode(question_index)
    session['image_index'] = jsonpickle.encode(image_index)


def retrieve_index_data():
    question_index = jsonpickle.decode(session['question_index'])
    image_index = jsonpickle.decode(session['image_index'])
    return question_index, image_index


def store_data(player, question_index, image_index):
    store_player_data(player)
    store_index_data(question_index, image_index)


def retrieve_data():
    player = retrieve_player_data()
    question_index, image_index = retrieve_index_data()
    return player, question_index, image_index
