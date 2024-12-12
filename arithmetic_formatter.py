# started: 05.12.2024
# finished: 05.12.2024


# https://www.freecodecamp.org/learn/scientific-computing-with-python/build-an-arithmetic-formatter-project/build-an-arithmetic-formatter-project
# Build an Arithmetic Formatter Project (Scientific Computing with Python 1/5)
# Finish the arithmetic_arranger function that receives a list of strings which are arithmetic problems, 
# and returns the problems arranged vertically and side-by-side. 
# The function should optionally take a second argument. 
# When the second argument is set to True, the answers should be displayed.
# ---------------------------------------------------------------------------------------------------------
# The function will return the correct conversion if the supplied problems are properly formatted.
# Otherwise, it will return a string that describes an error that is meaningful to the user.

# Situations that will return an error:
# - If there are too many problems supplied to the function. 
#   The limit is five, anything more will return: 'Error: Too many problems.'
# - The appropriate operators the function will accept are addition and subtraction. 
#   Multiplication and division will return an error. Other operators not mentioned in this bullet point will not need to be tested. 
#   The error returned will be: "Error: Operator must be '+' or '-'."
# - Each number (operand) should only contain digits. 
#   Otherwise, the function will return: 'Error: Numbers must only contain digits.'
# - Each operand (aka number on each side of the operator) has a max of four digits in width. 
#   Otherwise, the error string returned will be: 'Error: Numbers cannot be more than four digits.'
# - If the user supplied the correct format of problems, the conversion you return will follow these rules:
#     - There should be a single space between the operator and the longest of the two operands, 
#       the operator will be on the same line as the second operand, both operands will be in the same order as provided 
#       (the first will be the top one and the second will be the bottom).
#     - Numbers should be right-aligned.
#     - There should be four spaces between each problem.
#     - There should be dashes at the bottom of each problem. 
#       The dashes should run along the entire length of each problem individually.


def arithmetic_arranger(problems=[], show_answers=False):
    # rows for return string
    row1 = []
    row2 = []
    row3 = []
    row4 = []
    
    amount = len(problems)
    if amount <= 5:
        for term in problems:
            # splitting string into list for ease of use
            term = term.split()
            # checking for correct expression style
            if len(term) == 3:
                # checking for correct operators
                operator = term[1]
                if operator in ["+","-"]:
                    try:
                        strop1 = term[0]
                        strop2 = term[2]
                        # converts string operands to int, thereby checking if they only contain digits
                        op1 = int(strop1)
                        op2 = int(strop2)
                        longer = len(str(max([op1,op2])))
                        width = longer + 2
                        # checks if both operands are max 4 digits
                        if longer <= 4:
                            row1.append(f"{strop1:>{width}}")
                            row2.append(operator + f"{strop2:>{longer+1}}")
                            row3.append("-" * width)
                            
                            # calculates answers, if show_answers is True
                            if show_answers:
                                if term[1] == "+":
                                    result = str(op1 + op2)
                                else:
                                    result = str(op1 - op2)
                                row4.append(f"{result:>{width}}") 

                        else:
                            return 'Error: Numbers cannot be more than four digits.'
                    except:
                        return 'Error: Numbers must only contain digits.'
                else:
                    return "Error: Operator must be '+' or '-'."
        
        distance = "    "
        row1 = distance.join(row1)
        row2 = distance.join(row2)
        row3 = distance.join(row3)
        
        if show_answers:
            row4 = distance.join(row4)
            arrangement = [row1,row2,row3,row4]
        else:
            arrangement = [row1,row2,row3]
        arrangement = "\n".join(arrangement)
        return arrangement
    else:
        return 'Error: Too many problems.'



tests = [["3801 - 2", "123 + 49"],                                                 # 1
        ["1 + 2", "1 - 9380"],                                                     # 2
        ["3 + 855", "3801 - 2", "45 + 43", "123 + 49"],                            # 3
        ["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"],                # 4
        ["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"],    # 5     x
        ["3 / 855", "3801 - 2", "45 + 43", "123 + 49"],                            # 6     x
        ["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"],                         # 7     x
        ["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"],                           # 8     x
        ["3 + 855", "988 + 40"],                                                   # 9  true
        ["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"]]               # 10 true

for i in range(0,len(tests)):
    print(f'\n{arithmetic_arranger(tests[i])}')
    