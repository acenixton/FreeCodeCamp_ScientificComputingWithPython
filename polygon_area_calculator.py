# started: 11.12.2024
# finished: 11.12.2024 (ca. 1h)

# Build a Polygon Area Calculator Project

# In this project you will use object oriented programming to create a Rectangle class and a Square class. 
# The Square class should be a subclass of Rectangle, and inherit its methods and attributes.

# Rectangle class

# When a Rectangle object is created, it should be initialized with width and height attributes. 
# The class should also contain the following methods:
# set_width
# set_height
# get_area: Returns area (width * height)
# get_perimeter: Returns perimeter (2 * width + 2 * height)
# get_diagonal: Returns diagonal ((width ** 2 + height ** 2) ** .5)
# get_picture: Returns a string that represents the shape using lines of '*'. 
# The number of lines should be equal to the height and the number of '*' in each line should be equal to the width. 
# There should be a new line (\n) at the end of each line. 
# If the width or height is larger than 50, this should return the string: 'Too big for picture.'.
# get_amount_inside: Takes another shape (square or rectangle) as an argument. 
# Returns the number of times the passed in shape could fit inside the shape (with no rotations). 
# For instance, a rectangle with a width of 4 and a height of 8 could fit in two squares with sides of 4.
# Additionally, if an instance of a Rectangle is represented as a string, it should look like: 'Rectangle(width=5, height=10)'.


# Square class

# The Square class should be a subclass of Rectangle. 
# When a Square object is created, a single side length is passed in. 
# The __init__ method should store the side length in both the width and height attributes from the Rectangle class.
# The Square class should be able to access the Rectangle class methods but should also contain a set_side method. 
# If an instance of a Square is represented as a string, it should look like: 'Square(side=9)'.
# Additionally, the set_width and set_height methods on the Square class should set both the width and height.


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"
        
    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height
    
    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return self.width * 2 + self.height * 2
    
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5
    
    def get_picture(self):
        if self.width <= 50 and self.height <= 50:
            return "".join(["*" * self.width + "\n" for line in range(self.height)])
        else:
            return "Too big for picture."
        
    def get_amount_inside(self, shape):
        return int(self.width/shape.width) * int(self.height/shape.height)

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(width=side, height=side)
        
    def set_side(self, side):
        super().set_width(side)
        super().set_height(side)
    
    def set_width(self, width):
        self.width = width
        self.height = width
    
    def set_height(self, height):
        self.height = height
        self.width = height
        
    def __str__(self):
        return f"Square(side={self.width})"


### tests ###
rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))