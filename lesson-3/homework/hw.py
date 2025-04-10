# 1 exercise
fruits = ['strawberry','kiwi','apple','banana','blue berry']
fruit = fruits[2]
fruit

# 2 exercise
veget = ['potato','cucumber','carrot','corn','tomato']
fruits = ['strawberry','kiwi','apple','banana','blue berry']
fruits.extend(veget)
fruits

# 3 exercise
num = [1,2,3,4,5]
first = num[0]
middle = num[len(num)//2]
last = num[-1]
print(first, middle, last)

# 4 exercise
veget = ['potato','cucumber','carrot','corn','tomato']
tuple_opt = tuple(veget)
print(veget)

# 5 exercise
cities = ["New York", "Tokyo", "Tashkent", "London", "Dubai"]
if 'Paris' in cities:
  print('yeah')
else:
  print('nope')

# 6 exercise
numbers = ['1', '2', '3', '4']

x = numbers.copy()
x

# 7 exercise
numbers = ['1', '2', '3', '4']
numbers[0], numbers[-1] = numbers[-1], numbers[0]
numbers

#8 exercise
tupl_nums = tuple((1,2,3,4,5,6,7,8,9,10))
print(tupl_nums[2:8])

#9 exercise
colors = ['red', 'blue','green','blue','yellow','orange',]
blue = colors.count('blue')
blue

#10 exercise
animals = tuple(('tiger', 'wolf', 'baby', 'lion', 'bear'))
print(animals.index('lion'))

#11 exercise
animals = tuple(('1', '2', '3', '4', '5'))
dom_anim = tuple(('6', '7', '8', '9', '0'))
all = animals + dom_anim
all

# 12 exercise
numbers = ['1', '2', '3', '4']
animals = tuple(('tiger', 'wolf', 'baby', 'lion', 'bear'))
x = len(numbers)
y = len(animals)
print(x, y)

#13 exercise
animals = tuple(('tiger', 'wolf', 'baby', 'lion', 'bear'))
x = list(animals)
x

#14 exercise
animals = tuple((1,2,3,4,5,6,7,8,9))
x = max(animals)
y = min(animals)
print(x, y)

#15 exercise
animals = tuple(('tiger', 'wolf', 'baby', 'lion', 'bear'))
x = animals[::-1]
print(x)
