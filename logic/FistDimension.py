from models.Cell import Cell
import numpy as np


class FirstDimension:
    def __init__(self, width=100, iterations=100, rule=90):
        self.width = width
        self.iterations = iterations
        self.rule = rule
        self.game_array_current_state = self.initialize_array(width)
        self.game_array_previous_state = self.initialize_array(width)

    def initialize_array(self, width=100):
        tmp_array = []
        for column in list(range(width)):
            tmp_array.append(Cell(column + 1, False))

        return tmp_array

    def print_array(self, width=100, iterations=100):
        print("1D array")
        for column in range(width):
            print(self.game_array_current_state[column], end='')

    def calculate_value(self, index):
        sum = 2 ** 2 * (self.game_array_previous_state[index - 1].is_alive * 1) + 2 ** 1 * (self.game_array_previous_state[index - 1].is_alive * 1) + 2 ** 0 * (self.game_array_previous_state[index - 1].is_alive * 1)  # previous, current, following
        if sum == any([6, 4, 3, 1]):
            return True
        else:
            return False

    def next_iteration(self):
        self.game_array_previous_state = self.game_array_current_state
        self.initialize_array(self.game_array_current_state)
        for index in len(self.game_array_current_state):
            self.game_array_current_state[index].is_alive = self.calculate_value(index)
        self.print_array()
        print("\n")

    def begin_the_game(self):
        for iteration in range(self.iterations):
            self.next_iteration()