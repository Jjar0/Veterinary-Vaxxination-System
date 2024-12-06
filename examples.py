class Test:
    # Class variable holding string data
    variable = "I am a string"

    # Constructor with instance variables
    def __init__(self, name, number):
        self.name = name    # String variable
        self.number = number  # Integer variable

    # Method to display the variables
    def displayVariables(self):
        print(self.name)
        print(self.number)

# Creating an object
object = Test("Name", 7)

# Accessing variables and displaying them
object.displayVariables()