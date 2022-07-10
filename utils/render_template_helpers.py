import functools

import numpy as np
from flask import request

from utils.data_storage import retrieve_data


def render_wrapper(questions, new_question=False):

    def decorator(func):

        @functools.wraps(func)
        def inner():
            if new_question:
                ii = np.random.randint(0, len(questions))
            else:
                ii = int(request.form['question_index'])
            question = questions[ii]
            player = retrieve_data()
            return func(question, player)

        return inner

    return decorator
