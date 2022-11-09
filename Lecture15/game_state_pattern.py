"""
State Pattern in game with finite state machine that can change between three
game states
"""

import abc

class FSM:
    """
    FSM (Finite state machine) is the context. This will be the container that changes its states
    """
    def __init__(self, state):
        self.state = None # changes to multiple states
        self.running = True
        self.change_state(state)

    def change_state(self, state):
        """
        Changes the finite state machine's state
        :param state: the new state fsm is changing to use
        """
        if self.state is not None:
            self.state.end()  # clean up any code in the previous state

        self.state = state  # set the fsm's state to use the new state
        self.state.set_context(self)  # set the new state to point to the fsm
        print("\n---STATE CHANGED---\n")
        self.state.begin()  # call the new state's begin() function to do any state initialization code

    def update(self):
        # no code here that FSM does
        return self.state.update()

    def set_running(self, running):
        self.running = running

    def is_running(self):
        return self.running

class State(abc.ABC):
    """
    The abstract state class that contains references back to the context
    and methods to set the context
    """

    def __init__(self):
        self.context = None  # unique to the state pattern. states have a reference back to the context (FSM)

    def set_context(self, context):
        self.context = context # sets the context to point back at FSM

    @abc.abstractmethod
    def begin(self):
        pass

    @abc.abstractmethod
    def update(self):
        pass

    @abc.abstractmethod
    def end(self):
        pass

class MainMenu(State):
    """
    The concrete state. Each state performs different begin, end, and update function calls
    This state represents what happens when the enters the main menu
    The player has the option to start the game or quit the game
    """
    def __init__(self):
        super()

    def begin(self):
        print("Performing main menu initialization")
        print(' Show game title, button to quit game, button to start gameplay')

    def update(self):
        print("Performing main menu update")
        print("Press 1 - Enter gameplay")
        print("Press 2 - Quit")
        choice = int(input())
        if choice == 1:
            # unique to the state pattern. states have a reference back to the context (FSM)
            # this reference is used to call the context to change the state
            self.context.change_state(Gameplay())
            #code is here
        else:
            # unique to the state pattern. states have a reference back to the context (FSM)
            # this reference is used to call the context to stop running
            self.context.set_running(False)

    def end(self):
        print("Performing main menu clean up code")
        print(' close game title, button to quit game')

class Gameplay(State):
    """
    The concrete state. Each state performs different begin, end, and update function calls
    This state represents what happens when the player is actively playing during gameplay
    This is simulated by keeping the player alive, or having them die
    """
    def __init__(self):
        super()

    def begin(self):
        print("Performing gameplay initialization")
        print(' Show UI, health bars, scores')

    def update(self):
        print("Performing gameplay update")
        print("Press 1 - Player still alive")
        print("Press 2 - Player dies")
        choice = int(input())
        if choice == 2:
            # unique to the state pattern. states have a reference back to the context (FSM)
            # this reference is used to call the context to change the state
            self.context.change_state(GameOver())

    def end(self):
        print("Performing gameplay clean up code")
        print(' close UI, health bars, scores')

class GameOver(State):
    """
    The concrete state. Each state performs different begin, end, and update function calls
    This state represents what happens when the player dies in the game and is presented
    with a game over screen. The player has the option to return to the main menu or quit the game
    """
    def __init__(self):
        super()

    def begin(self):
        print("Performing game over initialization")
        print(' Show high score screens')

    def update(self):
        print("Performing game over update")
        print("Press 1 - Return to main menu")
        print("Press 2 - Quit")
        choice = int(input())
        if choice == 1:
            # unique to the state pattern. states have a reference back to the context (FSM)
            # this reference is used to call the context to change the state
            self.context.change_state(MainMenu())
        else:
            # unique to the state pattern. states have a reference back to the context (FSM)
            # this reference is used to call the context to stop running
            self.context.set_running(False)

    def end(self):
        print("Performing game over clean up code")
        print(' close high score screens')

def main():
    print("Create FSM and set first state to be Main Menu")
    fsm = FSM(MainMenu()) #sets the initial state of FSM to main menu

    # while the internal states don't set a boolean to stop the finite state machine
    # keep running updating the finite state machine
    while fsm.is_running():
         fsm.update()


if __name__ == '__main__':
    main()