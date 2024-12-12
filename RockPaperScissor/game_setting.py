import os
from player import Player


class GameSetting:
    def __init__(self):
        os.system("clear")

        print("==============================================================")
        print("Setting Menu")
        print("==============================================================")

        new_player_name = input("Input player name : ")
        Player.name = new_player_name
