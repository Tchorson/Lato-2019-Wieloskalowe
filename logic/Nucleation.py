from models.Cell import Cell
import os
import random
import numpy

class Nucleation:

    def __init__(self, width=15, height=10, iterations=10, pattern='homogeneous', periodical=True, neighbours = "Neumann",
                 seeds_amount = 5, width_amount = 3, height_amount = 2, radius = 5):
        self.width = width
        self.height = height
        self.iterations = iterations
        self.pattern = pattern
        self.game_array_current_state_2d = self.initialize_2d_array()
        self.game_array_previous_state_2d = self.initialize_2d_array()
        self.initial_states_2d = 'homogeneous,radius,random,manual'
        self.patterns_array = self.initial_states_2d.split(",")
        self.neighbours_states = 'Neumann,Hexagonal,Pentagonal,Radius'
        self.neighbours_array = self.neighbours_states.split(",")
        self.nucleation_neighbour = neighbours
        self.set_pattern_in_array(self.pattern)
        self.periodical = periodical
        self.last_iteration = False
        self.seeds_amount = seeds_amount # for random mode
        self.width_amount = width_amount # for homogeneous mode
        self.height_amount = height_amount # for homogeneous mode
        self.radius = radius

    def return_neighbour_array(self):
        return self.neighbours_array

    def search_for_zeros(self):
        self.last_iteration = True
        for row in range(self.height):
            for column in range(self.width):
                if self.game_array_current_state_2d[row][column].id == 0:
                    self.last_iteration = False

    def check_if_last_iteration(self):
        return self.last_iteration


    def initialize_2d_array(self):
        tmp_array = []
        for row in range(self.height):
            row_array = []
            for column in range(self.width):
                row_array.append(Cell(False))
            tmp_array.append(row_array)

        return tmp_array

    def calculate_value_2d(self, index_row, index_column):
        neighbour_index_array = [0,0,0,0]
        neighbour_amount_array = [0,0,0,0]
        current_row = index_row - 1
        current_column = index_column - 1
        dictionay = {}
        if self.periodical:
            for row_index in range(3):
                current_column = index_column - 1
                for column_index in range(3):
                    if current_row == index_row and current_column == index_column or \
                            current_row == index_row - 1 and current_column == index_column - 1 or \
                            current_row == index_row - 1 and current_column == index_column + 1 or \
                            current_row == index_row + 1 and current_column == index_column - 1 or \
                            current_row == index_row + 1 and current_column == index_column + 1:
                        current_column += 1
                        continue
                    neighbour_number = self.game_array_previous_state_2d[current_row % len(self.game_array_previous_state_2d)][current_column % len(self.game_array_previous_state_2d[0])].return_id()
                    if neighbour_number in neighbour_index_array:
                        neighbour_amount_array[neighbour_index_array.index(neighbour_number)]+=1
                    else:
                        new_neighbour_index = neighbour_index_array.index(0)
                        neighbour_index_array[new_neighbour_index] = self.game_array_previous_state_2d[current_row % len(self.game_array_previous_state_2d)][current_column % len(self.game_array_previous_state_2d[0])].return_id()
                        neighbour_amount_array[new_neighbour_index] +=1
                        dictionay[new_neighbour_index] = self.game_array_previous_state_2d[current_row % len(self.game_array_previous_state_2d)][current_column % len(self.game_array_previous_state_2d[0])].return_colours_array()
                    current_column += 1
                current_row += 1
        else:
            for row_index in range(3):
                current_column = index_column - 1
                for column_index in range(3):

                    if current_column >= len(self.game_array_previous_state_2d[0]) or current_row >= len(self.game_array_previous_state_2d) or current_column <0 or current_row <0:
                        current_column+=1
                        continue
                    if current_row == index_row and current_column == index_column or \
                            current_row == index_row - 1 and current_column == index_column - 1 or \
                            current_row == index_row - 1 and current_column == index_column + 1 or \
                            current_row == index_row + 1 and current_column == index_column - 1 or \
                            current_row == index_row + 1 and current_column == index_column + 1:
                        current_column +=1
                        continue
                    neighbour_number = self.game_array_previous_state_2d[current_row][current_column].return_id()
                    if neighbour_number in neighbour_index_array:
                        neighbour_amount_array[neighbour_index_array.index(neighbour_number)] += 1
                    else:
                        new_neighbour_index = neighbour_index_array.index(0)
                        neighbour_index_array[new_neighbour_index] = self.game_array_previous_state_2d[current_row][current_column].return_id()
                        neighbour_amount_array[new_neighbour_index] += 1
                        dictionay[new_neighbour_index] = self.game_array_previous_state_2d[current_row][current_column].return_colours_array()

                    current_column += 1
                current_row += 1

        dominant_neighbour_indexes = numpy.where(neighbour_amount_array == numpy.amax(neighbour_amount_array))[0]
        random_amount_index = random.choice(dominant_neighbour_indexes)
        return_index = neighbour_index_array[random_amount_index]
        return [return_index, dictionay.get(return_index)]


    def begin_the_game(self):
        for iteration in range(self.iterations):
            # print("iteration number ", iteration+1)
            self.next_iteration()

    def next_iteration(self):
        self.game_array_previous_state_2d = self.game_array_current_state_2d
        self.game_array_current_state_2d = self.initialize_2d_array()
        for row in range(len(self.game_array_previous_state_2d)):
            for column in range(len(self.game_array_previous_state_2d[row])):
                index_and_colors = self.calculate_value_2d(row, column)
                self.game_array_current_state_2d[row][column].set_id(index_and_colors[0])
                self.game_array_current_state_2d[row][column].set_colours_array(index_and_colors[1])
        return self.game_array_current_state_2d

    def return_current_array(self):
        return self.game_array_current_state_2d

    def return_previous_array(self):
        return self.game_array_previous_state_2d

    def set_iteration(self, iteration):
        self.iterations = iteration

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def return_height(self):
        return self.height

    def return_width(self):
        return self.width

    def return_iteration(self):
        return self.iterations

    def return_pattern(self):
        return self.pattern

    def set_current_array(self,array):
        self.game_array_current_state_2d = array

    def set_pattern_in_array(self, pattern):  # CHECK FOR WRONG ARRAY WRITE PROCESS
        self.game_array_current_state_2d = self.initialize_2d_array()

        if pattern in self.patterns_array:
            if pattern == 'homogeneous':

                pass

            if pattern == 'radius':
                pass

            if pattern == 'random':
                random_amount_of_seed = random.randint(1,self.seeds_amount)

                for iteration in range(random_amount_of_seed):
                    random_row = random.randint(1,self.height)
                    random_column = random.randint(1,self.width)

                    if (self.game_array_current_state_2d[random_row][random_column].id == 0):
                        random_red = random.randint(0, 255)
                        random_green = random.randint(0, 255)
                        random_blue = random.randint(0,255)

                        self.game_array_current_state_2d[random_row][random_column].id = iteration+1
                        self.game_array_current_state_2d[random_row][random_column].set_colours_array([random_red, random_green, random_blue])

                    else:
                        print(" iteration number: "+str(iteration)+" was not applied")

            if pattern == 'manual':
                pass
        else:
            self.game_array_current_state_2d = self.initialize_2d_array()
        #self.print_current_array()

    def set_parameters(self, width, height, iterations, pattern, periodical, neighbour, seeds_amount, width_amount, height_amount, radius):
        self.iterations = iterations
        self.periodical = periodical

        if pattern != self.pattern or self.width != width or self.height != height or self.periodical != periodical or \
                self.nucleation_neighbour != neighbour or self.seeds_amount != seeds_amount or\
                self.width_amount != width_amount or self.height_amount != height_amount or self.radius != radius:
            self.height_amount = height_amount
            self.width_amount = width_amount
            self.radius = radius

            self.height = height
            self.width = width
            self.seeds_amount = seeds_amount

            self.game_array_current_state_2d = self.initialize_2d_array()
            self.nucleation_neighbour = neighbour
            self.set_neighbour(self.nucleation_neighbour)
            self.pattern = pattern
            self.set_pattern_in_array(pattern)

    def set_seeds_amount(self,seeds):
        self.seeds_amount = seeds

    def return_seeds_amount(self):
        return self.seeds_amount

    def set_radius_amount(self,radius):
        self.radius = radius

    def return_radius_amount(self):
        return self.radius

    def set_width_amount(self,width):
        self.width_amount = width

    def return_width_amount(self):
        return self.width_amount

    def set_heigh_amount(self,height):
        self.height_amount = height

    def return_heigh_amount(self):
        return self.height_amount

    def set_neighbour(self,neighbour):
        if neighbour in self.neighbours_array:
            self.nucleation_neighbour = neighbour
        else:
            self.nucleation_neighbour = "Neumann"

    def restart_grid(self):
        self.game_array_current_state_2d = self.initialize_2d_array()
        self.set_neighbour(self.nucleation_neighbour)
        self.set_pattern_in_array(self.pattern)

    def return_parameters(self):
        return repr(self.height) + " " + repr(self.width) + " " + repr(self.iterations) +" "+ repr(self.periodical) + " " + repr(
            self.pattern) + " " + repr(self.game_array_previous_state_2d)

    def print_current_array(self):
        for row in range(len(self.game_array_current_state_2d)):
            for column in range(len(self.game_array_current_state_2d[row])):
                print(self.game_array_current_state_2d[row][column].is_alive, end=' ')

            print("\n")

    def set_current_array(self,array):
        self.game_array_current_state_2d = array

    def return_initial_array(self):
        return self.initialize_2d_array()

    def return_pattern_array(self):
        return self.patterns_array