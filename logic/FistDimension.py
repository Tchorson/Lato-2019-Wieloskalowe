from models.Cell import Cell


class FirstDimension:
    def __init__(self, width=100, iterations=100, rule=90):
        self.width = width
        self.iterations = iterations
        self.rule = rule
        self.rule_array = self.create_variables_for_speficic_rule(rule)
        self.game_array_current_state = self.initialize_array(width)
        self.game_array_previous_state = self.initialize_array(width)
        self.set_first_cell_alive()

    def create_variables_for_speficic_rule(self, rule):
        tmp_array = []
        while rule > 0:
            if rule >= 128:
                tmp_array.append(7)
                rule -= 128
            elif rule >= 64:
                tmp_array.append(6)
                rule -= 64
            elif rule >= 32:
                tmp_array.append(5)
                rule -= 32
            elif rule >= 16:
                tmp_array.append(4)
                rule -= 16
            elif rule >= 8:
                tmp_array.append(3)
                rule -= 8
            elif rule >= 4:
                tmp_array.append(2)
                rule -= 4
            elif rule >= 2:
                tmp_array.append(1)
                rule -= 2
            elif rule >= 1:
                tmp_array.append(0)
                rule -= 1

        print(tmp_array)
        return tmp_array

    def initialize_array(self, width=100):
        tmp_array = []
        for column in range(width):
            tmp_array.append(Cell(column + 1, False))

        return tmp_array

    def set_first_cell_alive(self):
        self.game_array_current_state[len(self.game_array_current_state) // 2].is_alive = True

    def calculate_value(self, index):
        sum = 2 ** 2 * (self.game_array_previous_state[index - 1].is_alive * 1) + 2 ** 1 * (
                self.game_array_previous_state[index].is_alive * 1) + 2 ** 0 * (self.game_array_previous_state[
                                                                                    (index + 1) % len(
                                                                                        self.game_array_previous_state)].is_alive * 1)  # previous, current, following
        # print("previous ",self.game_array_previous_state[index - 1].is_alive, " current ", self.game_array_previous_state[index].is_alive, " following ", self.game_array_previous_state[(index+1)%len(self.game_array_previous_state)].is_alive, " sum ", sum, " result ", sum == any([6, 4, 3, 1]))
        if sum in self.rule_array:  # any(first == c for c in letter) , if "a" in ["a", "b", "c"]:
            return True
        else:
            return False

    def begin_the_game(self):
        for iteration in range(self.iterations):
            # print("iteration number ", iteration+1)
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
