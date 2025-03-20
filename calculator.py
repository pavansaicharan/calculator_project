"""
A simple calculator program that performs basic arithmetic operations.
This module provides functions for addition, subtraction, multiplication,
and division, along with a command-line interface for user interaction.
"""

def add(a, b):
    """
    Add two numbers together.
    
    Args:
        a (float): The first number
        b (float): The second number
        
    Returns:
        float: The sum of a and b
    """
    return a + b

def subtract(a, b):
    """
    Subtract the second number from the first number.
    
    Args:
        a (float): The first number
        b (float): The second number
        
    Returns:
        float: The difference between a and b
    """
    return a - b

def multiply(a, b):
    """
    Multiply two numbers together.
    
    Args:
        a (float): The first number
        b (float): The second number
        
    Returns:
        float: The product of a and b
    """
    return a * b

def divide(a, b):
    """
    Divide the first number by the second number.
    
    Args:
        a (float): The numerator
        b (float): The denominator
        
    Returns:
        float or str: The quotient of a and b, or an error message if b is zero
    """
    if b == 0:
        return "Error! Division by zero."
    return a / b

def calculator():
    """
    Main calculator function that provides a command-line interface for user interaction.
    Allows users to choose between different arithmetic operations and input numbers.
    
    Returns:
        None
    """
    print("Simple Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    # Get user input for operation choice
    choice = input("Choose an operation (1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        # Get user input for numbers
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        # Perform the selected operation
        if choice == '1':
            print(f"Result: {add(num1, num2)}")
        elif choice == '2':
            print(f"Result: {subtract(num1, num2)}")
        elif choice == '3':
            print(f"Result: {multiply(num1, num2)}")
        elif choice == '4':
            print(f"Result: {divide(num1, num2)}")
    else:
        print("Invalid input!")

if __name__ == "__main__":
    calculator()
