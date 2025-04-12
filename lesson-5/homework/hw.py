#Determines whether a given year is a leap year.

year = int(input('enter a year:'))

if year % 4 == 0:
  print('that is a leap year')
elif year % 100 == 0 and year % 400 == 0:
  print('that is a leap year')
else:
  print('that is not a leap year')

#Given an integer, n, perform the following conditional actions:
number = int(input('enter a number:'))

if number % 2 == 0 and 6 <= number <= 20:
  print('Weird')
elif number % 2 == 0 and 2 <= number <= 5:
  print('Not Weird')
elif number % 2 == 0:
  print('Not Weird')
elif number % 2 != 0:
  print('Weird')
elif number % 2 == 0 and number > 20:
  print('Not Weird')


#Given two integer numbers a and b. Find even numbers between this numbers. a and b are inclusive. Don't use loop.

#Solution 1 with if-else statement.
a = int(input('enter a number'))
b = int(input('enter a number'))
evens = list(range(a if a % 2 == 0 else a + 1, b +1, 2))
print(evens)

#Solution 2 without if-else statement.
starting_number = int(input('enter a number'))
ending_number = int(input('enter a number'))
for i in range(starting_number + (starting_number % 2), ending_number+1, 2):
 print(i)
