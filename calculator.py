#Calculator

def add(n1,n2):
    """ This function will return addition"""
    return n1 + n2

def subtract(n1,n2):
    """ This function will return subtraction"""
    return n1 - n2

def multiply(n1,n2):
    """ This function will return multiplication"""
    return n1 * n2

def divide(n1, n2):
    """ This function will return division"""
    return n1 / n2

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

num1 = int(input("What's the first number:"))
num2 = int(input("What's the second number:"))

for symbol in operations:
    print(symbol)



