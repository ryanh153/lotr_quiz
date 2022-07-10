import functools

import numpy as np

from data_objects.questions import questions
from utils.data_storage import retrieve_data


def render_wrapper(func):

    @functools.wraps(func)
    def inner():
        ii = np.random.randint(0, len(questions))
        player = retrieve_data()
        question = questions[ii]
        return func(question, player)

    return inner
