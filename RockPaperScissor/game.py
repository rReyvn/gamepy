import os
from time import sleep

from player import Player
from game_setting import GameSetting


class Game:
    def __init__(self):
        self.menu()
        self.menu_action()

    def menu(self):
        os.system("clear")
        print("Hi! " + Player.name)
        print("==============================================================")
        print("Rock Paper Scissor")
        print("1. Start game")
        print("2. Settings")
        print("3. Exit")
        print("==============================================================")
        selected_choice = input("Choice (Type number to choose) : ")

        if selected_choice == "":
            print("Invalid choice, Please type number that available on the screen...")
            sleep(0.5)
            self.menu()
        else:
            self.menu_choice = int(selected_choice)

    def menu_action(self):
        if self.menu_choice == 1:
            print("Game Started!")
            sleep(1)
        if self.menu_choice == 2:
            GameSetting()
            Game()
        if self.menu_choice == 3:
            print("Game exited, See you again!")
            exit()
        else:
            print("Invalid choice, Please type number that available on the screen...")
