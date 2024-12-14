from os import system
from time import sleep
from player import Player, Computer
from menu import MainMenu
from move import Move


class Game:
    def __init__(self):
        MainMenu()
        self.start()

    def start(self):
        system("clear")
        self.player1 = Player()
        self.player2 = Computer()

        self.player1.choose_move(Move.PAPER)
        self.player2.choose_move(Move.SCISSOR)

        print(self.check_winner())

        sleep(1.5)

    def check_winner(self):
        if self.player1.move == self.player2.move:
            return "Tie!"
        elif Move.check(self.player1.move, self.player2.move):
            return f"{self.player1.name} win!"
        else:
            return f"{self.player2.name} win!"
