class Test:
    # Class variable holding string data
    variable = "I am a string"

    # Constructor with instance variables
    def __init__(self, name, numbers):
        self.name = name       # String variable
        self.numbers = numbers  # Array (list of integers)

    # Method to display the variables
    def displayVariables(self):
        print(self.name)
        print(self.numbers)

    # Method to calculate the sum of numbers
    def calculateSum(self):
        total = 0
        for num in self.numbers:  # Iteration through the array
            total += num          
        return total

    # Method to check if the sum is above or below a certain value
    def checkSum(self):
        total = self.calculateSum()
        if total > 50:  # Selection (branching)
            return "Sum is greater than 50"
        if total == 50:
            return "Sum is exactly 50"
        else:
            return "Sum is less than 50"

# Creating an object with an array of numbers
object = Test("Name", [10, 20, 5, 15])

# Accessing methods and demonstrating concepts
object.displayVariables()                   # Display name and numbers
print("Sum of Numbers>", object.calculateSum())  # Calculate and display the sum
print("Sum Check>", object.checkSum())           # Check and display sum condition
