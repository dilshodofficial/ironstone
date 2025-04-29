python -m venv myenv
myenv\Scripts\activate   
pip install numpy pandas 

def add(a, b):
    return a + b
def substract(a, b):
    return a - b
def multiply(a, b):
    return a*b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"

def reverse_text(text):
    return text[::-1]


def count_vowels(text):
    vowels = "aeiouAEIOU" 
    words = text.split()
    result = {}

    for word in words:
        count = sum(1 for letter in word if letter in vowels) 
        result[word] = count

    return result

geometry/
    __init__.py
    circle.py

import math
def calculate_circumference(radius):
  return 2*math.pi*radius

def calculate_area(radius):
  return math.pi*radius**2

file_operations/
    __init__.py
    file_reader.py
    file_writer.py

def read_file(file_path):
  with open(file_path, 'r') as file:
    return file.read()
  
def write_file(file_path, content):
  with open(file_path, 'w') as file:
    return file.write(content)
  
