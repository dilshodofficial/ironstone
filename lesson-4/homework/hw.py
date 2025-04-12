#Dictionary

#1 exercise
fruits_price = {'apple': 10, 'banana': 23, 'orange': 20, 'strawberry': 60}
sorted_desc = dict(sorted(fruits_price.items(), key=lambda x:x[1], reverse=True))
sorted_asc = dict(sorted(fruits_price.items(), key=lambda x:x[1], reverse=False))
print(sorted_desc, sorted_asc)

#2 exercise
numbers = {0: 10, 1: 20}
numbers.update({2: 30})
print(numbers)

#3 exercise
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
dic1.update(dic2)
dic1.update(dic3)
print(dic1)

#4 exercise
x = 1
y = int(input('ending numbers:'))
squares = {x: x*x ** 1 for x in range(x, y)}
print(squares)

#5 exercise
square_numbers = {x: x**2 for x in range(1, 16)}
print(square_numbers)

# Set
#1 exercise
numbers = set([1,2,3,4,4])
print(numbers)

#2 exercise
numbers = set([1,2,3,4,5,6,7,8,9])
for n in numbers:
  print(n)

#3 exercise
names = set(['jessica', 'donald', 'bob', 'kanye'])
names.add('kim')
print(names)

#4 exercise
fruits = set(['orange', 'apple', 'banana', 'peach'])
fruits.remove('peach')
print(fruits)

#5 exercise
vegetables = set({"carrot", "tomato", "cucumber", "pepper", "onion"})
if 'tomato' in vegetables:
  vegetables.remove('tomato')
else:
  pass
print(vegetables)
