class Player:
    name = "Player"

    def __init__(self):
        self.move = None

    def choose_move(self, move):
        self.move = move


class Computer(Player):
    name = "Computer"

    def __init__(self):
        self.move = None
