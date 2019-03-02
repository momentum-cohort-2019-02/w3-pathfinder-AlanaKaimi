""" 
A program for Using object-oriented programming and testing to read elevation data, draw an elevation map as a .png file, and chart the best path across the map.
"""
###* DONE: Read data from elevation_small.txt
###* DONE: Get data into appropriate list 
### TODO: Create elevation map (.png)
### TODO: Draw a path across it
    # Step 1: Read the data into a 2D array
    # Step 2: Find min, max elevations, and other calculations on the data  
    # Step 3: Draw the map
    # Step 4: Draw a lowest-elevation-change route starting from some row 
    # Step 5: Find and draw the lowest-elevation-change route in the map

import os 
from PIL import Image, ImageDraw, ImageColor

# ELEVATION_FILENAME = 'elevation_small.txt'

class MapData:
    """
    - Takes a file, opens and reads it
    - Creates a list of lists
    - Sorts data to find highest and lowest elevations
    -   
    """
    # filename = ELEVATION_FILENAME

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
###* <--- Should be good


### TODO: Working Here: ---->
class MapMaker:
    """
    - takes info from MapData and assigns colors to elevations
    - Makes Image 'map.png'
    """
    def __init__(self, map):
        self.map = map
        self.image_map = Image.new('RGBA', (600, 600))
    
    
    def make_map(self):
###* Reference: Changing Individual Pixels (in Automate python article)       
        for x in range(600[0]):
            for y in range(600):
                self.image_map.putpixel((x, y), (self.map.get_intensity(x, y), self.map.get_intensity(x, y), self.map.get_intensity(x, y)))
        self.image_map.save('map.png')

### TODO: Working Here: ^^^^^
###? Testing but: TypeError: 'int' object is not subscriptable

# class Pathfinder:
#     """ 
#     - Takes info from MapData
#     - Gives starting position
#     - Equation to find path
#     - Draws a path across the map
#     - Makes Image 'path.png'
#     """
#     def __init__(self, map):





#     def plot_path():
# ###* Reference pathfinder_janky.py https://github.com/momentum-cohort-2019-02/kb/blob/master/w3/examples/pathfinder_jank.py



#     def draw_path():
# ###* Drawing path(line) on map (Drawing on Images in Automate Python)



    # xxx.save("path.png", "PNG")
    

if __name__ == "__main__":
    
    map_info = MapData('elevation_small.txt')
    draw_map = MapMaker(map_info)
    draw_map.make_map()

# MapData(filename)