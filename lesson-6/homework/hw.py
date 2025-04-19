n = 0
number = 5

while n < number:
  print(n**2)
  n += 1

n = 0

while n in range(0, 10):
  print(abs(n))
  n += 1

i = 1
while i <= 5:
    j = 1
    while j <= i:
        print(j, end=' ')
        j += 1
    print()
    i += 1

number = 1
end_number = int(input('enter an ending number'))

for n in range(number, end_number):
  for digit in str(n):
    number += int(digit)
print(f"sum is: {number}")

n = 2
for i in range(1, 11):
  print(f"{n} x {i} = {n*i}")

numbers = [12, 75, 150, 180, 145, 525, 50]

for number in numbers:
  if number % 5 == 0 and number <= 150:
   print(number)
  if number % 5 == 0:
   break

number = int(input('enter a number'))
count = 0

while number > 0:
  count += 1
  number = number // 10
print(count)

i = 5
while i >= 1:
  j = 5
  while j >= 6 - i:
    print(j, end=' ')
    j -= 1
  print()
  i -= 1

list1 = [10, 20, 30, 40, 50]

for i in range(0, len(list1)-1):
    for j in range(i+1, len(list1)):
        if list1[i] < list1[j]:
            list1[i], list1[j] = list1[j], list1[i]
  
print(list1)

for x in range(-10, 0):
  print(x)

number = 0

while number < 5:
  print(number)
  if number == 6:
    break
  number = number + 1
else:
  print('Done!')

fact_number = int(input('enter a number'))
start = 1

for x in range(1, fact_number+1):
  start *= x
print(f"{fact_number}! = {start}")
