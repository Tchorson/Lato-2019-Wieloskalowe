from models.Cell import Cell
import os
import random
import numpy
import math

class Nucleation:

    def __init__(self, width=10, height=10, iterations=10, pattern='random', periodical=True, neighbours = "Neumann",
                 seeds_amount = 1, width_amount = 1, height_amount = 1, radius = 5):
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
        self.colors_dictionary = {}
        self.colors_dictionary[0]=[255,255,255]
        self.seeds_amount = seeds_amount # for random mode
        self.width_amount = width_amount # for homogeneous mode
        self.height_amount = height_amount # for homogeneous mode
        self.radius = radius
        self.last_iteration = False
        self.periodical = periodical

        self.set_pattern_in_array(self.pattern)
        self.set_neighbour(neighbours)


    def return_colors_dictionary(self):
        return self.colors_dictionary

    def set_colors_dictionary_element(self,index,array):
        self.colors_dictionary[index] = array

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
        dictionary = {}

        if self.periodical:
            if self.game_array_previous_state_2d[index_row][index_column].return_id() == 0:
                for row_index in range(3):
                    current_column = index_column - 1
                    for column_index in range(3):
                        if current_row == index_row and current_column == index_column or current_row == index_row - 1 and current_column == index_column - 1 or current_row == index_row - 1 and current_column == index_column + 1 or current_row == index_row + 1 and current_column == index_column - 1 or current_row == index_row + 1 and current_column == index_column + 1:
                            current_column += 1
                            continue
                        neighbour_number = self.game_array_previous_state_2d[current_row % len(self.game_array_previous_state_2d)][current_column % len(self.game_array_previous_state_2d[0])].return_id()
                        if neighbour_number != 0:
                            if neighbour_number in neighbour_index_array:
                                neighbour_amount_array[neighbour_index_array.index(neighbour_number)]+=1
                                if neighbour_number in self.colors_dictionary:
                                    dictionary[neighbour_number] = self.colors_dictionary.get(neighbour_number)
                                    pass
                                else:
                                    array_of_colours = \
                                    self.game_array_previous_state_2d[current_row % len(self.game_array_previous_state_2d)][
                                        current_column % len(self.game_array_previous_state_2d[0])].return_colours_array()
                                    self.colors_dictionary[neighbour_number] = array_of_colours
                                    dictionary[neighbour_number] = array_of_colours
                            else:
                                new_neighbour_index = neighbour_index_array.index(0)
                                neighbour_index_array[new_neighbour_index] = self.game_array_previous_state_2d[current_row % len(self.game_array_previous_state_2d)][current_column % len(self.game_array_previous_state_2d[0])].return_id()
                                neighbour_amount_array[new_neighbour_index] +=1
                                array_of_colours = self.game_array_previous_state_2d[current_row % len(self.game_array_previous_state_2d)][current_column % len(self.game_array_previous_state_2d[0])].return_colours_array()
                                dictionary[neighbour_number] = array_of_colours
                                if new_neighbour_index in self.colors_dictionary:
                                    dictionary[neighbour_number] = self.colors_dictionary.get(new_neighbour_index)
                                else:
                                    self.colors_dictionary[neighbour_number] = array_of_colours
                        current_column += 1
                    current_row += 1
            else:
                not_zero_index = self.game_array_previous_state_2d[index_row][index_column].return_id()
                return [not_zero_index, self.colors_dictionary.get(not_zero_index)]
        else:
            if self.game_array_previous_state_2d[index_row][index_column].return_id() == 0:
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
                            if neighbour_number in self.colors_dictionary:
                                dictionary[neighbour_number] = self.colors_dictionary.get(neighbour_number)
                                pass
                            else:
                                array_of_colours = self.game_array_previous_state_2d[current_row][current_column].return_colours_array()
                                self.colors_dictionary[neighbour_number] = array_of_colours
                                dictionary[neighbour_number] = array_of_colours
                        else:
                            new_neighbour_index = neighbour_index_array.index(0)
                            neighbour_index_array[new_neighbour_index] = self.game_array_previous_state_2d[current_row][current_column].return_id()
                            neighbour_amount_array[new_neighbour_index] += 1
                            array_of_colours = self.game_array_previous_state_2d[current_row][current_column].return_colours_array()
                            dictionary[new_neighbour_index] = array_of_colours
                            if new_neighbour_index in self.colors_dictionary:
                                dictionary[neighbour_number] = self.colors_dictionary.get(new_neighbour_index)
                            else:
                                self.colors_dictionary[neighbour_number] = array_of_colours
                        current_column += 1
                    current_row += 1
            else:
                not_zero_index = self.game_array_previous_state_2d[index_row][index_column].return_id()
                return [not_zero_index, self.colors_dictionary.get(not_zero_index)]

        #print(str(index_row)+" "+str(index_column))

        dominant_neighbour_indexes = numpy.where(neighbour_amount_array == numpy.amax(neighbour_amount_array))[0]
        random_amount_index = random.choice(dominant_neighbour_indexes)
        return_index = neighbour_index_array[random_amount_index]
        if return_index == 0:
            return[return_index, [255,255,255]]
        return [return_index, dictionary.get(return_index)]


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

                #print(str(index_and_colors[0])+"    "+str(index_and_colors[1]))
                self.game_array_current_state_2d[row][column].set_id(index_and_colors[0])
                self.game_array_current_state_2d[row][column].set_colours_array(index_and_colors[1])

        self.search_for_zeros()
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
        print("\n\n")
        #print("SET PATTERN")
        if pattern in self.patterns_array:
            if pattern == 'homogeneous':
                #     row_space = self.height/self.height_amount DOROBIC HOMOGENEOUS + RADIUS W GLOWNYM I PRZETESTOWAC
                #     column_space = self.width / self.height_amount

                height_disbalance = False
                width_disbalance = False

                if self.height_amount > self.height//2:
                    height_disbalance = True
                    space_between_rows = self.height//math.floor(self.height/2)
                    disbalanced_amount_in_rows = self.height - self.height//2
                    self.height_amount = math.floor(self.height / 2)
                else:
                    space_between_rows = self.height // self.height_amount
                    disbalanced_amount_in_rows = 0

                if self.width_amount > self.width//2:
                    width_disbalance = True
                    space_between_columns = self.width // math.floor(self.width / 2)
                    disbalanced_amount_in_columns = self.width - self.width // 2
                    self.width_amount = math.floor(self.width / 2)
                else:
                    space_between_columns = self.width // self.width_amount
                    disbalanced_amount_in_columns = 0


                iteration = 0



                if height_disbalance == 0 and width_disbalance == 0:
                    row_counter = space_between_columns//2
                    for index_row in range(self.height_amount):
                        column_counter = space_between_columns//2
                        for index_column in range(self.width_amount):
                            random_red = random.randint(0, 255)
                            random_green = random.randint(0, 255)
                            random_blue = random.randint(0, 255)
                            self.game_array_current_state_2d[row_counter][column_counter].id = iteration + 1
                            self.game_array_current_state_2d[row_counter][column_counter].set_colours_array([random_red, random_green, random_blue])
                            self.colors_dictionary[iteration + 1] = [random_red, random_green, random_blue]
                            column_counter+=space_between_columns
                            iteration+=1
                        row_counter+=space_between_rows


                if height_disbalance !=0 and width_disbalance !=0:
                    disbalanced_row_counter = 1
                    for disbalanced_index_row in range(disbalanced_amount_in_rows):
                        disbalanced_column_counter = 1
                        for disbalanced_index_column in range(disbalanced_amount_in_columns):
                            random_red = random.randint(0, 255)
                            random_green = random.randint(0, 255)
                            random_blue = random.randint(0, 255)
                            self.game_array_current_state_2d[disbalanced_row_counter][disbalanced_column_counter].id = iteration + 1
                            self.game_array_current_state_2d[disbalanced_row_counter][disbalanced_column_counter].set_colours_array(
                                [random_red, random_green, random_blue])
                            self.colors_dictionary[iteration + 1] = [random_red, random_green, random_blue]
                            disbalanced_column_counter += space_between_columns
                            iteration += 1
                        disbalanced_row_counter += space_between_rows

                if height_disbalance ==0 and width_disbalance !=0:
                    row_counter = 0
                    for index_row in range(self.height_amount):
                        disbalanced_column_counter = 1
                        for disbalanced_index_column in range(disbalanced_amount_in_columns):
                            random_red = random.randint(0, 255)
                            random_green = random.randint(0, 255)
                            random_blue = random.randint(0, 255)
                            self.game_array_current_state_2d[row_counter][disbalanced_column_counter].id = iteration + 1
                            self.game_array_current_state_2d[row_counter][disbalanced_column_counter].set_colours_array(
                                [random_red, random_green, random_blue])
                            self.colors_dictionary[iteration + 1] = [random_red, random_green, random_blue]
                            disbalanced_column_counter += space_between_columns
                            iteration += 1
                        row_counter += space_between_rows

                if height_disbalance !=0 and width_disbalance ==0:
                    disbalanced_row_counter = 1
                    for disbalanced_index_row in range(disbalanced_amount_in_rows):
                        column_counter = 1
                        for index_column in range(self.width_amount):
                            random_red = random.randint(0, 255)
                            random_green = random.randint(0, 255)
                            random_blue = random.randint(0, 255)
                            self.game_array_current_state_2d[disbalanced_row_counter][column_counter].id = iteration + 1
                            self.game_array_current_state_2d[disbalanced_row_counter][column_counter].set_colours_array(
                                [random_red, random_green, random_blue])
                            self.colors_dictionary[iteration + 1] = [random_red, random_green, random_blue]
                            column_counter += space_between_columns
                            iteration += 1
                        disbalanced_row_counter += space_between_rows

            if pattern == 'radius': # radius w menu glownym nie tu
                pass
            #print("BEFORE RANDOM")
            if pattern == 'random':

                for iteration in range(self.seeds_amount):
                    random_row = random.randint(0,len(self.game_array_current_state_2d)-1)
                    random_column = random.randint(0,len(self.game_array_current_state_2d[random_row])-1)
                    #print("ITERATION")
                    if (self.game_array_current_state_2d[random_row][random_column].id == 0):
                        random_red = random.randint(0, 255)
                        random_green = random.randint(0, 255)
                        random_blue = random.randint(0,255)

                        self.game_array_current_state_2d[random_row][random_column].id = iteration+1
                        #print("INSIDE1")
                        self.game_array_current_state_2d[random_row][random_column].set_colours_array([random_red, random_green, random_blue])
                        #print("INSIDE2")
                        self.colors_dictionary[iteration+1] = [random_red,random_green,random_blue]
                        #print("INSIDE3")
                    else:
                        print(" iteration number: "+str(iteration)+" was not applied")

            if pattern == 'manual':
                pass
        else:
            self.game_array_current_state_2d = self.initialize_2d_array()
        #self.print_current_array()

    def set_parameters(self, width, height, iterations, pattern, periodical, neighbour, seeds_amount, width_amount, height_amount, radius):
        self.iterations = iterations
        if periodical == "periodical":
            self.periodical = True
        else:
            self.periodical = False

        if pattern != self.pattern or self.width != width or self.height != height or self.periodical != periodical or \
                self.nucleation_neighbour != neighbour or self.seeds_amount != seeds_amount or\
                self.width_amount != width_amount or self.height_amount != height_amount or self.radius != radius:
            self.height_amount = height_amount
            self.width_amount = width_amount
            self.radius = radius

            self.height = height
            self.width = width
            self.seeds_amount = seeds_amount
            self.colors_dictionary.clear()

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
        self.colors_dictionary.clear()
        self.game_array_current_state_2d = self.initialize_2d_array()
        self.set_neighbour(self.nucleation_neighbour)
        #print("RESTART")
        self.set_pattern_in_array(self.pattern)


    def return_parameters(self):
        return repr(self.height) + " " + repr(self.width) + " " + repr(self.iterations) +" "+ repr(self.periodical) + " " + repr(
            self.pattern) + " " + repr(self.game_array_previous_state_2d)

    def print_current_array(self):
        #print("HERE")
        for row in range(len(self.game_array_current_state_2d)):
            for column in range(len(self.game_array_current_state_2d[row])):
                print(str(self.game_array_current_state_2d[row][column].return_id()), end=' ')

            print("\n")

    def set_current_array(self,array):
        self.game_array_current_state_2d = array

    def return_initial_array(self):
        return self.initialize_2d_array()

    def return_pattern_array(self):
        return self.patterns_array