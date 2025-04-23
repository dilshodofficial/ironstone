try:
  num1 = int(input('enter a number: '))
  num2 = int(input('enter a number you want to diveded by num1: '))
  result = num1/num2
  print(result)
except ZeroDivisionError:
  print('you cannot divide by zero')

try:
  num1 = int(input('enter a number: '))
  num2 = int(input('enter a number you want to diveded by num1: '))
  result = num1/num2
  print(result)
except ValueError:
  print('plz enter a number')

try:
  f = open("demotext.txt")
except FileNotFoundError:
  print('file doesnt exist')

try:
  number = int(input('enter a number'))
  if number < 10:
    print('thats not enough cuz thats type error')
  else:
    print(number)
except TypeError:
  print('TypeError occured right now')

number1 = int(input('enter a number'))
if number1 < 10:
  print('thats not enought ')
else:
  print(number1)

try:
  file = open('something.html')
  file
except PermissionError:
  print('u dont have permission to enter this file')

try:
  list = [1,2,3,4,5,6]
  list[6]
except IndexError:
  print('you are ot of index')

try:
  integer = int(input('enter a number'))
except KeyboardInterrupt:
  print('/nenter only a number bro')
except ValueError:
  print('bro write smth')

try:
  a = 12
  b = 0
  result = a/b
except ArithmeticError:
  print('thats arithmetic error brother')

try:
  f = open('unicode.css')
except UnicodeDecodeError:
  print('error has occured')

try:
  list = ['a', 'b', 'c', 'd']
  list.something()
except AttributeError:
  print('this list doesnt have this kind of method, please try another one')

f = open("name.txt", "rt")
print(f.read())

n = int(input('enter a number'))
f = open("name.txt", 'rt')
print(f.readline(n))

f = open("name.txt", "a")
f.write("\nhello")
f.close()

f = open("name.txt", "rt")
lines = f.readlines()
last = lines[-1]
print(last)

f = open("name.txt", 'rt')
f.readlines()
