import jsonpickle
from flask import session


def store_data(player):
    session['player'] = jsonpickle.encode(player)


def retrieve_data():
    return jsonpickle.decode(session['player'])
