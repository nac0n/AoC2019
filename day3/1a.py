# draw a matrix (for loop in for loop) and countdown coordinates to see  when the collisions occur, then look for the one closest to the starting point (0, 0)

import re
import numpy as np
import pandas as pd

class Wire():
    start_posX: 0
    start_posY: 0
    def __init__(self, instructions):
        self.instructions = instructions
        self.posX = 0
        self.posY = 0
        self.points = []
    def save_point(self, point):
        self.points.append(point)
    def setX(self, posX):
        self.posX = posX
    def setY(self, posY):
        self.posY = posY

def get_instructions_from_file():
    File_object = open("input.txt","r+")
    file_content = [x.strip() for x in File_object.readlines()]
    return file_content

def set_wires(wire1, wire2):
    for i in range(0, len(wire1.instructions)):
        instruction_split_array = re.split(r'(^[^\d]+)', wire1.instructions[i])[1:]
        direction = instruction_split_array[0]
        steps = int(instruction_split_array[1])
        for x in range(0, steps):
            if(direction == 'U'):
                wire1.setY(wire1.posY+1)
                wire1.save_point([wire1.posX, wire1.posY])
            if(direction == 'D'):
                wire1.setY(wire1.posY-1)
                wire1.save_point([wire1.posX, wire1.posY])
            if(direction == 'R'):
                wire1.setX(wire1.posX+1)
                wire1.save_point([wire1.posX, wire1.posY])
            if(direction == 'L'):
                wire1.setX(wire1.posX-1)
                wire1.save_point([wire1.posX, wire1.posY])
    for i in range(0, len(wire2.instructions)):
        instruction_split_array = re.split(r'(^[^\d]+)', wire2.instructions[i])[1:]
        direction = instruction_split_array[0]
        steps = int(instruction_split_array[1])
        for x in range(0, steps):
            if(direction == 'U'):
                wire2.setY(wire2.posY+1)
                wire2.save_point([wire2.posX, wire2.posY])
            if(direction == 'D'):
                wire2.setY(wire2.posY-1)
                wire2.save_point([wire2.posX, wire2.posY])
            if(direction == 'R'):
                wire2.setX(wire2.posX+1)
                wire2.save_point([wire2.posX, wire2.posY])
            if(direction == 'L'):
                wire2.setX(wire2.posX-1)
                wire2.save_point([wire2.posX, wire2.posY])

def get_wires_intersections(wire1, wire2):
    intersections = []
    w1 = np.array(wire1.points);
    w2 = np.array(wire2.points);

    print(w1, w2)
    # # if wire1 array är kortare
    # if(len(w1) < len(w2)):
    #     for i in range(0, len(wire1.points)):
    #         for x in range(0, len(wire2.points)):
    #             if(wire1.points[i] == wire2.points[x]):
    #                 intersections.append(wire1.points[i])
    # # if wire2 array är kortare
    # elif(len(w2) < len(w1)):
    #     for i in range(0, len(wire2.points)):
    #         for x in range(0, len(wire1.points)):
    #             if(wire2.points[i] == wire1.points[x]):
    #                 intersections.append(wire2.points[i])
    return intersections

def get_closest_intersection(intersections):
    for i in range(0, len(intersections)):
        added_intersection_number = abs(intersections[i][0]) + abs(intersections[i][1])
        if(i == 0 ):
            lowest_number = added_intersection_number
        else:
            if(lowest_number > added_intersection_number):
                lowest_number = added_intersection_number
    return lowest_number

def start():
    input = get_instructions_from_file()
    wire1_instructions = input[0].split(',')
    wire2_instructions = input[1].split(',')
    wire1 = Wire(wire1_instructions)
    wire2 = Wire(wire2_instructions)
    set_wires(wire1, wire2)
    intersections = get_wires_intersections(wire1, wire2)
    if(len(intersections) > 0 ):
        print(get_closest_intersection(intersections))

start()
