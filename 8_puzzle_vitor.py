import sys

from copy import deepcopy


class Node:

    def __init__(self, state, misplaced_pieces):
        self.state = state
        self.misplaced_pieces = misplaced_pieces


def ask_initial_state():
    # Get puzzle initial state from user
    puzzle = []
    print("Enter inital state separated by spaces. Example: 1 2 3 4 5 6 8 7 _")
    input_data = input().split()
    if not len(input_data) == 9:
        return False
    puzzle.append(input_data[0:3])
    puzzle.append(input_data[3:6])
    puzzle.append(input_data[6:9])
    return puzzle


def number_of_misplaced_pieces(initial):
    misplaced = 0
    for i in range(3):
        for j in range(3):
            if initial[i][j] != goal_state[i][j] and initial[i][j] != '_':
                misplaced += 1
    return misplaced


def find_free_position(current_state):
    for i in range(3):
        for j in range(3):
            if current_state[i][j] == '_':
                return i, j
    return


def remove_impossible_moves(directions):
    for direction in directions:
        if (direction[0] > 2 or direction[1] > 2) or (direction[0] < 0 or direction[1] < 0):
            directions.remove(direction)
    return directions


def solve_uniform_cost(current_state):
    # Use only cost, without heuristic. In this case, cost is the number of misplaced pieces.
    i, j = find_free_position(current_state)
    directions = [[i, j - 1], [i, j + 1], [i - 1, j], [i + 1, j]]
    directions = remove_impossible_moves(directions)
    copies = []
    for direction in directions:
        # In this case, just current_state.copy() wasn't enough. Copy would still get reference from current_state
        # and altering copy, would result in altering current_state as well. Deepcopy solves it.
        copy = deepcopy(current_state)
        copy[i][j], copy[direction[0]][direction[1]] = current_state[direction[0]][direction[1]], '_'
        copies.append({'state': copy, 'misplaced_pieces': number_of_misplaced_pieces(copy)})

    lower_misplaced = 100
    for copy in copies:
        if copy.get('misplaced_pieces') < lower_misplaced:
            lower_misplaced = copy.get('misplaced_pieces')
            current_state = copy.get('state')

    print(3)


def solve_a_star_simple(puzzle):
    # Use cost + heuristic. In this case, heuristic is the number of moves made so far.
    pass


def solve_a_star_manhattan_distance_heuristic(puzzle):
    # To improve heuristics, when neighboring straight-line pieces goals are
    # in inverse, multiply cost + heuristic value by 1,5.
    pass


def solve_a_star_first_line_ordered_heuristic(puzzle):
    # if first line is already ordered, you are not allowed to move any pieces of the first line [1, 2, 3]
    # if my_list[0].is_ordered():
    #     for elements in my_list[0]:
    #         elements.freeze()
    pass


if __name__ == '__main__':
    goal_state = [['1', '2', '3'],
                  ['4', '5', '6'],
                  ['7', '8', '_']]
    paths_to_goal = []
    initial_state = ask_initial_state()
    if not initial_state:
        print('Your input must have exactly 9 elements.')
        sys.exit()
    print('Your initial puzzle state is: \n %s \n %s \n %s' % (initial_state[0], initial_state[1], initial_state[2]))
    print('The goal state is: \n %s \n %s \n %s' % (goal_state[0], goal_state[1], goal_state[2]))
    solve_uniform_cost(initial_state)
