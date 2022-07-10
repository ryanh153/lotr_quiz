import jsonpickle
from flask import session

from data_objects.player import Player


def store_data(player: Player):
    session['player'] = jsonpickle.encode(player)


def retrieve_data() -> Player:
    return jsonpickle.decode(session['player'])
