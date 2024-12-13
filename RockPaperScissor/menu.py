from os import system
from time import sleep
from player import Player


class Menu:
    def __init__(self, title, opts):
        self.title = title
        self.opts = opts

        self.printMenu()

    def printHeader(self):
        print("==============================================================")
        print(self.title)
        print("==============================================================")

    def printOption(self):
        for index, opt in enumerate(self.opts, start=1):
            print(f"{index}. {opt}")

    def menuChoice(self):
        selected_choice = input("Choice (Type number to choose) : ")

        if selected_choice == "":
            print("Invalid choice, Please type number that available on the screen...")
            sleep(0.5)
            self.printMenu()
        else:
            self.menu_choice = int(selected_choice)

    def printMenu(self):
        system("clear")
        self.printHeader()
        self.printOption()
        self.menuChoice()


class MainMenu(Menu):
    def __init__(self):
        super().__init__("Rock Paper Scissor", ["Start Game", "Setting", "Exit"])
        self.menuAction()

    def printHeader(self):
        print(Player().name)
        print("==============================================================")
        print(self.title)
        print("==============================================================")

    def menuAction(self):
        if self.menu_choice == 1:
            self.__init__()
        if self.menu_choice == 2:
            SettingMenu()
            self.__init__()
        if self.menu_choice == 3:
            print("Game exited, See you again!")
            exit()
        else:
            print("Invalid choice, Please type number that available on the screen...")


class SettingMenu(Menu):
    def __init__(self):
        super().__init__("Setting", ["Change Player Name", "Back"])
        self.menuAction()

    def menuAction(self):
        if self.menu_choice == 1:
            self.player_name_setting()
            self.__init__()
        if self.menu_choice == 2:
            return
        else:
            print("Invalid choice, Please type number that available on the screen...")

    def player_name_setting(self):
        system("clear")
        self.printHeader()
        new_player_name = input("Input player name : ")
        Player.name = new_player_name
