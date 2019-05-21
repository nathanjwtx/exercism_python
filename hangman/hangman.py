# Game status categories
# Change the values as you see fit
STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"


class Hangman(object):
    def __init__(self, word):
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        self.word = word
        self.result = ["_"] * len(self.word)

    def guess(self, char):
        if self.remaining_guesses < 0:
            self.status = STATUS_LOSE
            raise ValueError("Guess limit reached")
        elif self.status == STATUS_WIN:
            raise ValueError("Game over man! It's game over!")
        else:
            blanks = self.result.count("_")
            for x in range(0, len(self.word)):
                if self.word[x] == char:
                    self.result[x] = char
            if blanks == self.result.count("_"):
                self.remaining_guesses -= 1

    def get_masked_word(self):
        return "".join(self.result)

    def get_status(self):
        if self.result.count("_") > 1 and self.remaining_guesses < 0:
            self.status = STATUS_LOSE
        elif self.remaining_guesses >= 0 and self.word == "".join(self.result):
            self.status = STATUS_WIN
        else:
            self.status = STATUS_ONGOING
        return self.status

    def get_guesses(self):
        return self.remaining_guesses
