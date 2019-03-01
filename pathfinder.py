""" 
A program for Using object-oriented programming and testing to read elevation data, draw an elevation map as a .png file, and chart the best path across the map.
"""
### TODO: Read data from elevation_small.txt
### TODO: Get data into appropriate structure 
### TODO: Create elevation map (.png)
### TODO: Draw a path across it
    # Step 1: Read the data into a 2D array
    # Step 2: Find min, max elevations, and other calculations on the data  
    # Step 3: Draw the map
    # Step 4: Draw a lowest-elevation-change route starting from some row 
    # Step 5: Find and draw the lowest-elevation-change route in the map

# import os ?
# from PIL import Image, ImageDraw, ImageColor

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
        # return self.get_elevation(x, y) / self.max_elevation * 255
        return int((self.get_elevation(x, y) - self.min_elevation) / (self.max_elevation - self.min_elevation) * 255)   


class MapMaker:
    """
    - takes info from MapData and assigns colors to elevations
    - Makes Image 'map.png'
    """
    def __init__(self, map):
        self.map = map
        self.image_map = Image.new('RGBA', (600, 600))
    
    
    def make_map(self):
    
    pass
###* Changing Individual Pixels (in Automate python article)
    # image_map.save('map.png')


class Pathfinder:
    """ 
    - Takes info from MapData
    - Gives starting position
    - Equation to find path
    - Draws a path across the map
    - Makes Image 'path.png'
    """
    pass
###* Drawing path(line) on map (Drawing on Images in Automate Python)
    # xxx.save("path.png", "PNG")
    

if __name__ == "__main__":
    
    filename = ('elevation_small.txt')

MapData(filename)
    
    # pass