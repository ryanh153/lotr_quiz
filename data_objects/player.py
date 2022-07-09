from dataclasses import dataclass


@dataclass
class Player:
    current_streak: int = 0
    longest_streak: int = 0
    n_correct: int = 0
    n_incorrect: int = 0

    def correct_answer(self):
        self.current_streak += 1
        self.n_correct += 1
        if self.current_streak > self.longest_streak:
            self.longest_streak = self.current_streak

    def incorrect_answer(self):
        self.current_streak = 0
        self.n_incorrect += 1

    @property
    def n_answered(self):
        return self.n_correct + self.n_incorrect

    @property
    def win_percentage_str(self):
        if not self.n_answered:
            return '0 %'
        return f'{round(100.*(self.n_correct / self.n_answered))} %'


player = Player()
