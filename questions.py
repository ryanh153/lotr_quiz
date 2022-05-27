from dataclasses import dataclass
from typing import Tuple


@dataclass
class Question:
    question: str
    options: Tuple[str, str, str, str]
    answer: int
    index: int = 0


without_indices = [
    Question(question="On which day did Aragorn and the Captains arrive at the walls of Minas Tirith, after the "
                      "War of the Ring?",
             options=("Midsummer's eve", "The Eve of May", "The first day of Spring", "The first of April"),
             answer=1),

    Question(question="On what day did the Fair Folk out of the north arrive at the Gates of Minas Tirith?",
             options=("The Eve of Midsummer", "The first of April", "22nd September", "25th December"),
             answer=0),

    Question(question="How were the leftover hobbits taken away from the Long-expected Party?",
             options=("In barrels", "In vans", "On toboggans", "In wheelbarrows"),
             answer=3),
]

questions = list()
for ii, q in enumerate(without_indices):
    q.index = ii
    questions.append(q)