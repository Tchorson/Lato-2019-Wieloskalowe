import numpy as np

class Cell:
    is_alive = False
    id = 0
    colours = [255, 255, 255]
    weight_center = [0.0, 0.0]

    def __init__(self, input_alive = False, colours = [255,255,255], weight_center = [-1,-1],energy = -1):
        self.is_alive = input_alive
        self.colours = colours
        self.weight_center = weight_center
        self.energy = energy

    def __eq__(self, other):
        if isinstance(other,self.__class__):
            return self.id == other.id and self.colours == other.colours and self.weight_center == other.weight_center

    def __ne__(self, other):
        return self.id != other.id or self.colours != other.colours or self.weight_center != other.weight_center

    def __repr__(self):
        #return repr(self.__id) + " " + repr(self.is_alive) + " "
        return repr(self.id) + " "

    def return_state(self):
        return self.is_alive

    def set_id(self,input_id):
        self.id = input_id

    def set_weight_center(self,weight_center):
        self.weight_center = weight_center

    def set_energy(self,energy):
        self.energy = energy

    def return_energy(self):
        return self.energy

    def return_weight_center(self):
        return self.weight_center

    def set_state(self, alive_state):
        self.is_alive = alive_state

    def set_colours_array(self, colours_array):
        self.colours = colours_array

    def return_colours_array(self):
        return self.colours

    def set_colour(self,index,value):
        self.colours[index]=value

    def set_red(self,value):
        self.colours[0] = value

    def set_green(self,value):
        self.colours[1] = value

    def set_blue(self,value):
        self.colours[2] = value

    def return_id(self):
        return self.id
