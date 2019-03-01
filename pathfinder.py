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
from PIL import Image

ELEVATION_FILENAME = 'elevation_small.txt'

class MapData:
    """
    - Takes a file, opens and reads it
    - Creates a list of lists
    - Sorts data to find highest and lowest elevations
    -   
    """
    filename = ELEVATION_FILENAME

    with open(filename) as file:
        elevation_data = [line.strip() for line in file]
    pass

class MapDrawer:
    """
    - takes info from MapData and assigns colors to elevations
    - Makes Image 'map.png'
    """
    pass

class Pathfinder:
    """ 
    - Takes Map
    - Gives starting position
    - Equation to find path
    - Draws a path across the map
    - Makes Image 'path.png'
    """
    
    pass
