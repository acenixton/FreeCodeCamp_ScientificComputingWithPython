# started: 11.12.2024
# finished: 

# Build a Probability Calculator Project

# For this project, you will write a program to determine the approximate probability of drawing certain balls randomly from a hat.

# First, create a Hat class in main.py. 
# The class should take a variable number of arguments that specify the number of balls of each color that are in the hat.

# A hat will always be created with at least one ball. 
# The arguments passed into the hat object upon creation should be converted to a contents instance variable. 
# Contents should be a list of strings containing one item for each ball in the hat. 
# Each item in the list should be a color name representing a single ball of that color. 
# For example, if your hat is {'red': 2, 'blue': 1}, contents should be ['red', 'red', 'blue'].

# The Hat class should have a draw method that accepts an argument indicating the number of balls to draw from the hat. 
# This method should remove balls at random from contents and return those balls as a list of strings. 
# The balls should not go back into the hat during the draw, similar to an urn experiment without replacement. 
# If the number of balls to draw exceeds the available quantity, return all the balls.

# Next, create an experiment function in main.py (not inside the Hat class). 
# This function should accept the following arguments:

# hat: A hat object containing balls that should be copied inside the function.
# expected_balls: An object indicating the exact group of balls to attempt to draw from the hat for the experiment. 
# For example, to determine the probability of drawing 2 blue balls and 1 red ball from the hat, set expected_balls to {'blue':2, 'red':1}.
# num_balls_drawn: The number of balls to draw out of the hat in each experiment.
# num_experiments: The number of experiments to perform. 
# (The more experiments performed, the more accurate the approximate probability will be.)

# The experiment function should return a probability.

# For example, if you want to determine the probability of getting at least two red balls and one green ball 
# when you draw five balls from a hat containing six black, four red, and three green. 
# To do this, you will perform N experiments, count how many times M you get at least two red balls and one green ball, 
# and estimate the probability as M/N. 
# Each experiment consists of starting with a hat containing the specified balls, 
# drawing several balls, and checking if you got the balls you were attempting to draw.



import copy
import random

class Hat:
    def __init__(self, *, yellow=None, blue=None, green=None, red=None, orange=None, black=None, pink=None, striped=None):
        # gets all given argument variables in dictionary
        balls = {**locals()}
        # removes the Hat itself so only the balls remain
        balls.pop('self')
        if any(balls):
            pass 
        

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    pass

sombrero = Hat()