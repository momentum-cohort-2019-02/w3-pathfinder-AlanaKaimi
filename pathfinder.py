""" 
A program for Using object-oriented programming and testing to read elevation data, draw an elevation map as a .png file, and chart the best path across the map.
"""
###* DONE: Read data from elevation_small.txt
###* DONE: Get data into appropriate list 
###* DONE: Create elevation map (.png)
### TODO: Draw a path across it

import os 
from PIL import Image, ImageDraw, ImageColor
from pprint import pprint

class MapData:
    """
    - Takes a file, opens and reads it
    - Creates a list of lists
    - Sorts data to find highest and lowest elevations
    -   
    """

    def __init__(self, filename):
        self.elevations = [ ]

        with open(filename) as file:
            for line in file:
                self.elevations.append([int(e) for e in line.split()])
        
        self.max_elevation = max([max(row) for row in self.elevations])
        self.min_elevation = min([min(row) for row in self.elevations])

###! Printing to see remove later --->
        # print(self.elevations) <-- prints HUGE list
        print(self.max_elevation)
        print(self.min_elevation)
###! <--- remove
    def get_elevation(self, x, y):
        return self.elevations[y][x]

    def get_intensity(self, x, y):
    
        return int((self.get_elevation(x, y) - self.min_elevation) / (self.max_elevation - self.min_elevation) * 255)   

class MapMaker:
    """
    - takes info from MapData and assigns colors to elevations
    - Makes Image 'map.png'
    """
    def __init__(self, map):
        self.map = map
        self.image_map = Image.new('RGBA', (len(self.map.elevations[0]), len(self.map.elevations)))
    
    
    def make_map(self):
###* Reference: Changing Individual Pixels (in Automate python article)       
        for x in range(len(self.map.elevations[0])):
            for y in range(len(self.map.elevations)):
                self.image_map.putpixel((x, y), (self.map.get_intensity(x, y), self.map.get_intensity(x, y), self.map.get_intensity(x, y)))
        self.image_map.save('map.png')


### TODO: --->
class Pathfinder:
    """ 
    - Takes info from MapData
    - Gives starting position
    - Equation to find path
    - Draws a path across the map
    - Makes Image 'path.png'
    """
    def __init__(self, map):
        self.map = map
        



    def plot_path():
###* Reference pathfinder_janky.py https://github.com/momentum-cohort-2019-02/kb/blob/master/w3/examples/pathfinder_jank.py
        while cur_x < len(elevations[0]) - 1:
    print("---")
    possible_ys = [cur_y]
    if cur_y - 1 >= 0:
        possible_ys.append(cur_y - 1)
    if cur_y + 1 < len(elevations):
        possible_ys.append(cur_y + 1)

    diffs = [
        abs(elevations[poss_y][cur_x + 1] - elevations[cur_y][cur_x])
        for poss_y in possible_ys
    ]

    min_diff = min(diffs)
    min_diff_index = diffs.index(min_diff)
    next_y = possible_ys[min_diff_index]

    cur_x += 1
    cur_y = next_y


    def draw_path(self, xy, fill, width):
###* Drawing path(line) on map (Drawing on Images in Automate Python)
        im_path = Image.new('RGBA' (600, 600) 'teal')
        draw = ImageDraw.Draw(im_path)

        draw.line([(0, 0), (599, 599), (0, 599), (0, 0)], fill='teal')



        xxx.save("path.png", "PNG")
    

if __name__ == "__main__":
    
    map_info = MapData('elevation_small.txt')
    draw_map = MapMaker(map_info)
    draw_map.make_map()
