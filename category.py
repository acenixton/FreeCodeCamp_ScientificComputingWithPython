# 09.12.2024

# https://www.freecodecamp.org/learn/scientific-computing-with-python/build-a-budget-app-project/build-a-budget-app-project
# Build a Budget App Project (Scientific Computing with Python 3/5)
# Complete the Category class. 
# It should be able to instantiate objects based on different budget categories like food, clothing, and entertainment. 
# When objects are created, they are passed in the name of the category. 
# The class should have an instance variable called ledger that is a list. 

# The class should also contain the following methods:

# A deposit method that accepts an amount and description. 
# If no description is given, it should default to an empty string. 
# The method should append an object to the ledger list in the form of {'amount': amount, 'description': description}.

# A withdraw method that is similar to the deposit method, but the amount passed in should be stored in the ledger as a negative number. 
# If there are not enough funds, nothing should be added to the ledger. 
# This method should return True if the withdrawal took place, and False otherwise.

# A get_balance method that returns the current balance of the budget category based on the deposits and withdrawals that have occurred.

# A transfer method that accepts an amount and another budget category as arguments. 
# The method should add a withdrawal with the amount and the description 'Transfer to [Destination Budget Category]'. 
# The method should then add a deposit to the other budget category with the amount and the description 'Transfer from [Source Budget Category]'. 
# If there are not enough funds, nothing should be added to either ledgers. 
# This method should return True if the transfer took place, and False otherwise.

# A check_funds method that accepts an amount as an argument. 
# It returns False if the amount is greater than the balance of the budget category and returns True otherwise. 
# This method should be used by both the withdraw method and transfer method.

# When the budget object is printed it should display:

# A title line of 30 characters where the name of the category is centered in a line of * characters.

# A list of the items in the ledger. Each line should show the description and amount. 
# The first 23 characters of the description should be displayed, then the amount. 
# The amount should be right aligned, contain two decimal places, and display a maximum of 7 characters.

# A line displaying the category total.

# Besides the Category class, create a function (outside of the class) called create_spend_chart that takes a list of categories as an argument. 
# It should return a string that is a bar chart.

# The chart should show the percentage spent in each category passed in to the function. 
# The percentage spent should be calculated only with withdrawals and not with deposits. 
# Down the left side of the chart should be labels 0 - 100. 
# The 'bars' in the bar chart should be made out of the 'o' character. 
# The height of each bar should be rounded down to the nearest 10. 
# The horizontal line below the bars should go two spaces past the final bar. 
# Each category name should be written vertically below the bar. 
# There should be a title at the top that says 'Percentage spent by category'.

# This function will be tested with up to four categories.

class Category:
    
    def __init__(self, name):
        self.name = name
        self.ledger = []
    
    def __str__(self):
        totst = "Total"
        printout = f"{self.name:*^30}\n"
        for i in self.ledger:
            printout += f"{i['description']:23.23}{i['amount']:>7.2f}\n"
        printout += f"{totst}: {self.get_balance()}"
        return printout    
        
    def deposit(self,amount,description=""):
        self.ledger.append({'amount': amount, 'description': description})
    
    def withdraw(self,amount,description=""):
        if self.check_funds(amount):
            self.ledger.append({'amount': amount * -1, 'description': description})
            return True
        else:
            return False
        
    def transfer(self,amount,other_category):
        if self.check_funds(amount):
            self.withdraw(amount,f"Transfer to {other_category.name}")
            other_category.deposit(amount,f"Transfer from {self.name}")
            return True
        else:
            return False
    
    def get_balance(self):
        return sum([val['amount'] for val in self.ledger])
    
    def check_funds(self,amount):
        return amount <= self.get_balance()


# barchart for expenses
def create_spend_chart(categories):
    # getting total of expenses in each category
    sumtotal = 0
    expenses = []
    for cat in categories:
        spent = 0
        for val in cat.ledger:
            if val['amount'] < 0:
                spent += abs(val['amount'])
        expenses.append(spent)
        sumtotal += spent
    
    # calculating percentage of every category and rounding to nearest decade
    percentages = []
    for ex in expenses:
        percentages.append(int(ex/sumtotal * 10)*10)
    
    # setup for return string
    title = "Percentage spent by category"
    chartlist = ["  0|"," 10|"," 20|"," 30|"," 40|"," 50|"," 60|"," 70|"," 80|"," 90|","100|",]
    
    # adds bars to chart
    for i in range(0,len(chartlist)):
        
        for p in percentages:
            if p >= i * 10:
                chartlist[i] += " o "
            else:
                chartlist[i] += "   "
        chartlist[i] += " "
    chartlist.append(title)
    chartlist.reverse()
    
    # adds line under bars
    linelen = len(categories) * 3 + 1
    chartlist.append("    " + "-" * linelen )
    
    # generating label strings
    names = [cat.name for cat in categories]
    namelen = max([len(name) for name in names])
    labels = []
    labelstring = "" 
    # adding white space so all names are the same length
    for n in names:
        labels.append(list(n + " " * (namelen - len(n))))
    
    # reordering letters so the words are vertical
    # after last letter 2 spaces
    for j in range(0,namelen):
        labelstring += "\n     " + "  ".join([label[j] for label in labels]) + "  "

    # assembling final string
    chart = "\n".join(chartlist) + labelstring
    return chart


### testing ###

food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)
catlist = [food,clothing]
print(create_spend_chart(catlist))