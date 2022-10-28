import abc
import enum


# setup screen enums
class ScreenEnum(enum.Enum):
    MAIN_MENU = 1
    GAMEPLAY = 2
    GAME_OVER = 3


# Classes representing screens
class Screen(abc.ABC):
    @abc.abstractmethod
    def show_screen(self):
        pass


class MainMenu(Screen):
    def show_screen(self):
        print("Show Main Menu screen")
        print("Show start button")
        print("Show options button")


class Gameplay(Screen):
    def show_screen(self):
        print("Show Gameplay screen")
        print("Show gameplay info")
        print("Show pause button")


class GameOver(Screen):
    def show_screen(self):
        print("Show GameOver screen")
        print("Show high score")
        print("Show quit button")


class ScreenManager:
    __instance = None

    @staticmethod
    def get_instance():
        if ScreenManager.__instance is None:
            ScreenManager()
        return ScreenManager.__instance

    def show_screen(self, screen : ScreenEnum):
        # calls screen in dictionary to show
        ScreenManager.__instance.screens[screen].show_screen()

    def __init__(self):
        if ScreenManager.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            ScreenManager.__instance = self

            # initialize screens in singleton instance
            ScreenManager.__instance.screens = {}
            ScreenManager.__instance.screens[ScreenEnum.MAIN_MENU] = MainMenu()
            ScreenManager.__instance.screens[ScreenEnum.GAMEPLAY] = Gameplay()
            ScreenManager.__instance.screens[ScreenEnum.GAME_OVER] = GameOver()


# Various calls to ScreenManager in different areas of game code
# First call in main menu logic
s = ScreenManager.get_instance()
s.show_screen(ScreenEnum.MAIN_MENU)
print(s)

# 2nd call in gameplay logic
print("-" * 20)
s1 = ScreenManager.get_instance()  # gets the one instance of singleton no matter how many times called
s1.show_screen(ScreenEnum.GAMEPLAY)
print(s1)

# 3rd call at end of gameplay logic
print("-" * 20)
s2 = ScreenManager.get_instance()  # gets the one instance of singleton no matter how many times called
s2.show_screen(ScreenEnum.GAME_OVER)
print(s2)