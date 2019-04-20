from models.Cell import Cell
import numpy as np


class FirstDimension:
    def __init__(self, width=100, iterations=100, rule=90):
        self.width = width
        self.iterations = iterations
        self.rule = rule
        self.game_array_current_state = self.initialize_array(width)
        self.game_array_previous_state = self.initialize_array(width)
        self.set_first_cell_alive()

    def initialize_array(self, width=100):
        tmp_array = []
        for column in range(width):
            tmp_array.append(Cell(column + 1, False))

        return tmp_array

    def set_first_cell_alive(self):
        self.game_array_current_state[len(self.game_array_current_state) // 2].is_alive=True

    def calculate_value(self, index):
        sum = 2 ** 2 * (self.game_array_previous_state[index - 1].is_alive * 1) + 2 ** 1 * (self.game_array_previous_state[index].is_alive * 1) + 2 ** 0 * (self.game_array_previous_state[(index + 1)%len(self.game_array_previous_state)].is_alive * 1)  # previous, current, following
        #print("previous ",self.game_array_previous_state[index - 1].is_alive, " current ", self.game_array_previous_state[index].is_alive, " following ", self.game_array_previous_state[(index+1)%len(self.game_array_previous_state)].is_alive, " sum ", sum, " result ", sum == any([6, 4, 3, 1]))
        if sum in [6, 4, 3, 1]: # any(first == c for c in letter) , if "a" in ["a", "b", "c"]:
            return True
        else:
            return False

    def begin_the_game(self):
        for iteration in range(self.iterations):
            #print("iteration number ", iteration+1)
            self.next_iteration()

    def next_iteration(self):
        self.game_array_previous_state = self.game_array_current_state
        self.game_array_current_state = self.initialize_array(len(self.game_array_current_state))
        for index in range(len(self.game_array_current_state)):
            self.game_array_current_state[index].is_alive = self.calculate_value(index)
        self.print_array()
        print("\n")

    def print_array(self, width=100, iterations=100):
        for column in range(width):
            print(self.game_array_previous_state[column], end='')