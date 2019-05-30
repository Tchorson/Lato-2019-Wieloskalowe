import random,math,numpy

class MonteCarlo:

    def __init__(self,iterations,kt,periodical,neighbour_pattern):
        print("Object created!")
        self.iterations = iterations
        self.kt = kt
        self.periodical = periodical
        self.neighbour_pattern = neighbour_pattern
        self.pattern_offsets = {
            'Neumann': [[-1, 0], [0, -1], [1, 0], [0, 1]],  # row, column
            'PentagonalUp': [[-1, 1], [-1, 0], [-1, -1], [0, -1], [0, 1]],
            'PentagonalDown': [[1, -1], [1, 0], [1, 1], [0, -1], [0, 1]],
            'PentagonalRight': [[-1, 1], [0, 1], [1, 1], [-1, 0], [1, 0]],
            'PentagonalLeft': [[-1, -1], [0, -1], [1, -1], [-1, 0], [1, 0]],
            'HexagonalL': [[-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0]],
            'HexagonalR': [[-1, 0], [-1, -1], [0, -1], [0, 1], [1, 1], [1, 0]],
            'Moore': [[-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [-1, -1], [1, 1]],
        }
        self.border_seed_energy = 1
        self.shuffled_coordinates_array = numpy.array([[row, column] for row in range(self.height) for column in range(self.width)])

    def set_generated_microstructure(self,generated_microstructure,height,width):
        self.height = height
        self.width = width
        self.generated_microstructure = generated_microstructure

    def set_parameters(self,neighbour,kt,iterations,periodical):
        if self.neighbour_pattern != neighbour or self.kt != kt or self.iterations != iterations or self.periodical != periodical:
            self.neighbour_pattern = neighbour
            self.kt = kt
            self.iterations = iterations
            self.periodical = periodical

    def iteration(self): #Todo, GUI, connect gui in main file
        random.shuffle(self.shuffled_lcoordinates_array)
        
        for random_coordinates in self.shuffled_coordinates_array:
            random_row = random_coordinates[0]
            random_column = random_coordinates[1]

            dictionary = {}

            energy_before = 0
            array_of_stuff = self.pattern_offsets[self.neighbour_pattern]

            for item in array_of_stuff:
                current_row = random_row + item[0]
                current_column = random_column + item[1]

                if self.periodical:
                    if self.generated_microstructure[current_row % self.height][current_column % self.width].return_id() in dictionary:
                        dictionary[self.generated_microstructure[current_row % self.height][current_column % self.width].return_id()][0] += 1
                    else:
                        dictionary[self.generated_microstructure[current_row % self.height][current_column % self.width].return_id()] = [1, [self.generated_microstructure[current_row % self.height][
                                current_column % self.width].return_colours_array()]]

                    if self.generated_microstructure[current_row % self.height][current_column % self.width].return_id() != self.generated_microstructure[random_row % self.height][
                        random_column % self.width].return_id():
                            energy_before += 1

                else:
                    if not self.height > current_row >= 0 or not self.width > current_column >= 0:
                        continue

                    if self.generated_microstructure[current_row][current_column].return_id() in dictionary:
                        dictionary[self.generated_microstructure[current_row][current_column].return_id()][0] += 1
                    else:
                        dictionary[self.generated_microstructure[current_row][current_column].return_id()] = [1, [self.generated_microstructure[current_row][current_column].return_colours_array()]]

                    if self.generated_microstructure[current_row][current_column].return_id() != self.generated_microstructure[random_row][random_column].return_id():
                        energy_before += 1

            random_index, amount_and_colors = random.choice(list(dictionary.items()))

            energy_after = 8 - amount_and_colors[0]

            if self.find_minimal_energy(energy_after - energy_before):
                self.generated_microstructure[random_row][random_column].set_id(random_index)
                self.generated_microstructure[random_row][random_column].set_colours_array(amount_and_colors[1])

            self.generated_microstructure[random_row][random_column].set_energy(energy_before)
        return self.generated_microstructure

    def find_minimal_energy(self,delta_energy):
        if delta_energy <=0:
            return True
        else:
            if random.randint(0,100) < math.exp(-delta_energy/self.kt):
                return True
        return False

    def set_iterations(self, iterations):
        self.iterations = iterations

    def set_kt(self, kt):
        self.kt = kt

    def set_periodical(self, periodical):
        self.periodical = periodical

    def set_neighbour_pattern(self, neighbour_pattern):
        self.neighbour_pattern = neighbour_pattern

    def return_iterations(self):
        return self.iterations

    def return_kt(self):
        return self.kt

    def return_periodical(self):
        return self.periodical

    def return_neighbour_pattern(self):
        return self.neighbour_pattern