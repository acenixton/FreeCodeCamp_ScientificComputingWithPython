# started: 11.12.2024
# finished: 12.12.2024

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
    # uses kwargs wrapper because the colors and amount of colors can be chosen by the caller
    def __init__(self, **kwargs):
        self.contents = []
        for color in kwargs.keys():
            # adds given amount of every color ball
            self.contents.extend([color for _ in range(kwargs[color])])
        
    def draw(self, tries):
        if tries < len(self.contents):
            balls = [self.contents.pop(random.randint(0,len(self.contents)-1)) for _ in range(tries)]
        else:
            balls = copy.copy(self.contents)
            self.contents.clear()
        print(f"pool: {self.contents}\ndrawn: {balls}")
        return balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    met_results = 0
    for _ in range(num_experiments):
        hatcopy = copy.deepcopy(hat)
        current_draw = hatcopy.draw(num_balls_drawn)
        exp_results = [current_draw.count(color) >= expected_balls[color] for color in expected_balls.keys()]
        if all(exp_results):
            met_results += 1
    return met_results / num_experiments
        

sombrero = Hat(yellow=5, red=7, blue=8)
# print(sombrero.draw(5))
print(experiment(sombrero, {'blue':1, 'red':2}, 3, 8))