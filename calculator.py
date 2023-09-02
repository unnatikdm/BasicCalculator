#!/usr/bin/env python
# coding: utf-8

# In[8]:


#solves overall huge equations
def equations():
    equation = input("Enter the equation: ")
    try:
        return eval(equation)
    except Exception as e:
        print("Error:", e)
    
#solves basic equatons
def basic():
    symbol = None  
    operations = ["+", "-", "*", "/"]
    #taking input
    n = input("Enter a basic operation: ")
    #searching symbol and splitting equation
    for op in operations:
        if op in n:
            symbol = op
            n = n.split(op)
            break  # Exit the loop if an operation is found
    
    if symbol is None:
        print("Operation not recognized.")
    
    try:
        a = int(n[0])
        b = int(n[1])
    except ValueError:
        print("Invalid input for numbers.")
        return 0
    
    if symbol == '+':
        return a + b
    elif symbol == '-':
        return a - b
    elif symbol == '*':
        return a * b
    elif symbol == '/':
        if b == 0:
            print("Division by zero is not allowed.")
            return 0
        return a / b
    else:
        print("Operation not recognized.")
        return 0

check = int(input("Click 1 for equation and 2 for basic operation: "))

if check == 1:
    answer = equations()
elif check == 2:
    answer = basic()
else:
    print("Warning! Choose 1 or 2")

print("Result:", answer)

