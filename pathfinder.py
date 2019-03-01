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
# from PIL import Image

# ELEVATION_FILENAME = 'elevation_small.txt'

class MapData:
    """
    - Takes a file, opens and reads it
    - Creates a list of lists
    - Sorts data to find highest and lowest elevations
    -   
    """
    # filename = ELEVATION_FILENAME

    def elevations(self, filename):

        self.elevation_data = []
        with open(filename) as file:
            for line in file:
                self.elevation_data.append([int(e) for e in line.strip().split(" ")])
            return self

        print(self)

MapData()


class MapDrawer:
    """
    - takes info from MapData and assigns colors to elevations
    - Makes Image 'map.png'
    """

###* Changing Individual Pixels (in Automate python article)
    xxx.save("map.png", "PNG")
    pass

class Pathfinder:
    """ 
    - Takes Map
    - Gives starting position
    - Equation to find path
    - Draws a path across the map
    - Makes Image 'path.png'
    """
    
###* Drawing path(line) on map (Drawing on Images in Automate Python)
    xxx.save("path.png", "PNG")
    pass

if __name__ == "__main__":
    
    
    
    pass