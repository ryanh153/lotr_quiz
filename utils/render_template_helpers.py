import functools
import logging
from dataclasses import dataclass
from pathlib import Path

import numpy as np

from data_objects.images import load_images
from data_objects.player import Player
from data_objects.questions import load_questions, Question
from utils.data_storage import retrieve_data, store_index_data

questions = load_questions()
images = load_images()
logger = logging.getLogger(__name__)


@dataclass
class PageData:
    player: Player
    question: Question
    image: Path


def render_wrapper(new_question=False):

    def decorator(func):

        @functools.wraps(func)
        def inner():
            if new_question:
                qi = np.random.randint(0, len(questions))
                ii = np.random.randint(0, len(images))
                store_index_data(qi, ii)
                logger.debug(f'New question/image {qi} / {ii}')

            player, qi, ii = retrieve_data()
            page_data = PageData(player, questions[qi], images[ii])
            return func(page_data)

        return inner

    return decorator
