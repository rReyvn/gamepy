from enum import Enum


class Move(Enum):
    ROCK = 1
    PAPER = 2
    SCISSOR = 3

    @staticmethod
    def check(p1_move, p2_move):
        if (
            (p1_move == Move.ROCK and p2_move == Move.SCISSOR)
            or (p1_move == Move.PAPER and p2_move == Move.ROCK)
            or (p1_move == Move.SCISSOR and p2_move == Move.PAPER)
        ):
            return True

        return False
