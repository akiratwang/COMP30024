"""
Team: _blank_ 
player.py to hold our player class
"""
# Import Dependencies
from moves import *

# Global Variables
INITIAL_PIECE_COUNT = 4
INITIAL_EXITED_PIECES = 0



class Tet: # lmao the default is ExamplePlayer
    def __init__(self, colour):
        """
        This method is called once at the beginning of the game to initialise
        your player. You should use this opportunity to set up your own internal
        representation of the game state, and any other information about the 
        game state you would like to maintain for the duration of the game.

        The parameter colour will be a string representing the player your 
        program will play as (Red, Green or Blue). The value will be one of the 
        strings "red", "green", or "blue" correspondingly.
        """
        # TODO: Set up state representation.
        self.state = None # state["pieces"] returns array of our pieces, state["enemy"] returns array of blocked pieces?
        self.colour = colour
        """
        self.strategy = default to book learning / max^n / paranoid / directed offence
        """
        self.pieces = INITIAL_PIECE_COUNT # Can add or subtract depending on captured
        self.exited_pieces = INITIAL_EXITED_PIECES


    def action(self):
        """
        This method is called at the beginning of each of your turns to request 
        a choice of action from your program.

        Based on the current state of the game, your player should select and 
        return an allowed action to play on this turn. If there are no allowed 
        actions, your player must return a pass instead. The action (or pass) 
        must be represented based on the above instructions for representing 
        actions.
        """
        # TODO: Decide what action to take.
        #### AKIRA
        # Action is a representation of the most recent action (or pass) conforming to the above instructions for representing actions

        
        return ("PASS", None)


    def update(self, colour, action):
        """
        This method is called at the end of every turn (including your player’s 
        turns) to inform your player about the most recent action. You should 
        use this opportunity to maintain your internal representation of the 
        game state and any other information about the game you are storing.

        The parameter colour will be a string representing the player whose turn
        it is (Red, Green or Blue). The value will be one of the strings "red", 
        "green", or "blue" correspondingly.

        The parameter action is a representation of the most recent action (or 
        pass) conforming to the above instructions for representing actions.

        You may assume that action will always correspond to an allowed action 
        (or pass) for the player colour (your method does not need to validate 
        the action/pass against the game rules).
        """
        # TODO: Update state representation in response to action.
        #### I assume we update our own piece for the move we take so 
        #### If not our colour, update state with their action
