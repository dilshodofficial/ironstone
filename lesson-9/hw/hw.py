class Cirlce:
  def __init__(self, r):
    self.r = r
  def area(self):
    p = 3.141
    print(f"The area of circle equals {p * self.r**2}")

  def perimeter(self):
    p = 3.141
    print(f"The perimeter of circle equals to {2*p*self.r}")

first = Cirlce(5)
first.area()
first.perimeter()


class Person:
  def __init__(self, name, country, dateofbirth):
    self.name = name
    self.country = country
    self.dateofbirth = dateofbirth
  
  def name(self):
    print(self.name)

  def country(self):
    print(self.country)
  
  def age(self):
    import datetime

    x = datetime.datetime.now()
    print(x.year - self.dateofbirth)

p1 = Person('Dilshod', "Uzb", 2009)
p1.age()
p1.name()
p1.country()

class Calculator:
  def __init__(self, a, b):
    self.a = a
    self.b = b
  def plus(self):
    print(self.a + self.b)
  def minus(self):
    print(self.a - self.b)
  def multiply(self):
    print(self.a * self.b)
  def divide(self):
    print(self.a / self.b)

numbers = Calculator(4, 2)
numbers.plus()
numbers.minus()
numbers.multiply()
numbers.divide()

class Shape:
  def area(self):
    pass
  def perimeter(self):
    pass
class square(Shape):
  def __init__(self, a):
    self.a = a
  def area(self):
    print(self.a**2)
  def perimeter(self):
    print(4*self.a)
class triangle:
  def __init__(self, a, b, c):
    self.a = a
    self.b = b
    self.c = c
  def perimeter(self):
    return self.a + self.b + self.c
  def area(self):
    return (self.a + self.b + self.c) / 2
class circle:
  def __init__(self, r):
    self.r = r
  def perimeter(self):
    p = 3.141
    return 2*p*self.r
  def area(self):
    p = 3.141
    return p*(self.r**2)
  
p = square(5)
p1 = circle(5)
p2 = triangle(1,2,3)

p1.area()
p.area()
p2.area()

class Stack:
  def __init__(self):
    self.items = []

  def push(self, item):
    self.items.append(item)

  def pop(self, items):
    if not self.is_empty():
      return self.items.pop()
    else:
      return None  
  
  def is_empty(self):
    self.len(self.items) == 0

class Shopping:
  def __init__(self):
    self.products = {}

  def adding(self, name, price):
    self.products[name] = price

  def removing(self, name):
    if name in self.products:
      del self.products[name]
    else:
      return None
      
  def total_sum(self):
    total = sum(self.products.values())
    return total

class Queue:
  def __init__(self):
    self.items = []
  def enqueue(self, item):
    self.items.append(item)
  def dequeue(self):
    if not self.is_empty(): 
      self.items.pop(0)
    else:
      return None
  def is_empty(self):
    return len(self.items) == 0
  def list(self):
    for x in self.items:
      print(x)

class Bank:
    def __init__(self):
        self.accounts = {}

    def add_customer(self, name, initial_balance=0):
        if name not in self.accounts:
            self.accounts[name] = initial_balance
            print(f"Customer {name} added with balance {initial_balance}.")
        else:
            print(f"Customer {name} already exists.")

    def deposit(self, name, amount):
        if name in self.accounts:
            self.accounts[name] += amount
            print(f"{amount} deposited to {name}'s account.")
        else:
            print(f"Customer {name} not found.")

    def withdraw(self, name, amount):
        if name in self.accounts:
            if self.accounts[name] >= amount:
                self.accounts[name] -= amount
                print(f"{amount} withdrawn from {name}'s account.")
            else:
                print("Insufficient funds.")
        else:
            print(f"Customer {name} not found.")

    def check_balance(self, name):
        if name in self.accounts:
            print(f"{name}'s balance is {self.accounts[name]}")
            return self.accounts[name]
        else:
            print(f"Customer {name} not found.")
            return None
