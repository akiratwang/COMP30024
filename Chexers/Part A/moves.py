from collections import defaultdict
from classes import *

######################### GLOBALS #########################

# Goals for each player
GOAL = defaultdict(list)
GOAL["red"].append([[3,r] for r in range(-3, 1)])
GOAL["blue"].append([[-3,0],[-2,1],[-1,2],[0,3]])
GOAL["green"].append([[q,3] for q in range(-3, 1)])

# Game valid coordinate positions
## Taken from the test generator script
""" Made it in caps so we know its a global variable """
VALID_COORDINATES = [[-3, 0], [-3, 1], [-3, 2], [-3, 3],
                    [-2, -1], [-2, 0], [-2, 1], [-2, 2], [-2, 3],
                    [-1, -2], [-1, -1], [-1, 0], [-1, 1], [-1, 2], [-1, 3],
                    [0, -3], [0, -2], [0, -1], [0, 0], [0, 1], [0, 2], [0, 3],
                    [1, -3], [1, -2], [1, -1], [1, 0], [1, 1], [1, 2],
                    [2, -3], [2, -2], [2, -1], [2, 0], [2, 1],
                    [3, -3], [3, -2], [3, -1], [3, 0]]

# Partly adapted from https://www.redblobgames.com/grids/hexagons/#neighbors-axial
""" Made it in caps so we know its a global variable """
POSSIBLE_DIRECTIONS = [[0,1],[1,0],[1,-1],[0,-1],[-1,0],[-1,1]]

######################### FUNCTIONS #########################

# Returns goals given player colour
def find_goal(player, data):

    # ***TEMPORARY*** # Default player goal
    player_goal = GOAL[player][0]

    # Check if goal not blocked by piece(s)
    non_movable = data["blocks"] + data["pieces"]

    """ updated this so that it counts your own pieces too """
    player_goal = [i for i in player_goal if i not in non_movable]

    return player_goal

# Possible moves from current location
def possible_moves(data, player_goal, debug_flag = False):
    player_pieces = data["pieces"]
    for piece in player_pieces:
        # All possible move actions to a coordinate in nested list form
        possible_moves = move(piece, data, debug_flag)

        # All possible jump actions to a coordinate in nested list form
        possible_jumps = jump(piece, data, debug_flag)

        # Checks if the current hex is eligible for an exit action
        exit_possible = exit_move(piece, player_goal)

        print("Player coordinate: ", piece)
        print("Possible Move Action to:", possible_moves)
        print("Possible Jump Action to:", possible_jumps)
        print("*" * 40)

# Retrieves adj hexes that are in valid coordinates
def adj_hex(coordinate):
    return [Vector.add(coordinate, x) for x in POSSIBLE_DIRECTIONS if
        Vector.add(coordinate, x) in VALID_COORDINATES]

# Finds possible move actions given a coordinate
def move(coordinate, data, debug_flag = False):
    # Non-movable pieces on board
    non_movable = data["blocks"] + data["pieces"]
    possible_moves = list()

    for direction in POSSIBLE_DIRECTIONS:
        adjacent_hex = Vector.add(coordinate, direction)
        if adjacent_hex in VALID_COORDINATES: # Then it's not off-board
            if adjacent_hex not in non_movable: # Then it's free for the taking
                possible_moves.append(adjacent_hex)
            elif (debug_flag):
                print("OCCUPIED - CANNOT MOVE to", adjacent_hex)
        elif (debug_flag):
            print("OFF-BOARD - CANNOT MOVE")

    return possible_moves

# Finds possible jump actions given a coordinate
"""You had it as Debug_flag and it kept giving errors lelelele"""
def jump(coordinate, data, debug_flag = False):
    # Non-movable pieces on board
    non_movable = data["blocks"] + data["pieces"]
    possible_jumps = list()

    for direction in POSSIBLE_DIRECTIONS:
        adjacent_hex = Vector.add(coordinate, direction)
        target_hex = Vector.add(adjacent_hex, direction)
        # ONLY NESTED FOR DEBUGGING PURPOSES
        if adjacent_hex in non_movable: # Then you can jump over it
            if target_hex in VALID_COORDINATES: # Then not off-board
                if target_hex not in non_movable: # Then actual place to land
                    possible_jumps.append(target_hex)
                elif (debug_flag):
                    print("HEX OCCUPIED - CANNOT JUMP over", adjacent_hex)
            elif (debug_flag):
                print("OFF BOARD - CANNOT JUMP")

    return possible_jumps

# Determines if exit action possible
def exit_move(coordinate, player_goal):
    exit_possible = (coordinate in player_goal)
    print("Exit Action Possible? ", exit_possible)

    return exit_possible
