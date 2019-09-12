import sys


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


def solve_uniform_cost(initial, goal):
    # Use only cost, without heuristic. In this case, the cost is number of misplaced pieces.
    pass


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
    initial_state = ask_initial_state()
    if not initial_state:
        print('Your input must have exactly 9 elements.')
        sys.exit()
    goal_state = [['1', '2', '3'], ['4', '5', '6'], ['8', '7', '_']]
    print('Your initial puzzle state is: \n %s \n %s \n %s' % (initial_state[0], initial_state[1], initial_state[2]))
    print('The goal state is: \n %s \n %s \n %s' % (goal_state[0], goal_state[1], goal_state[2]))
    solve_uniform_cost(initial_state, goal_state)
