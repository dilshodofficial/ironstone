# 1 exercise
name = input("whats your name?")
age = int(input("how old are you?"))
print(f"My name is {name}, i am {age}")

# 2 exercise
txt = 'LMaasleitbtui'
car = txt[1:13:2], txt[0:13:2]
print(car)

# 3 exercise
txt = 'MsaatmiazD'
car = txt[-1] + txt[-3] + txt[-5] + txt[-8] + txt[-9], txt[0] + txt[2] + txt[4] + txt[6] + txt[-2]
print(car)

# 4 exercise
txt = "I'am John. I am from London"
extr = txt[21:27]
print(extr)

# 5 exercise
txt = "basketball"
rev = txt[::-1]
print(rev)

# 6 exercise
word = input('write a word')
vowels = 'aeiouyAEIOUY'
count = sum(word.count(vowel) for vowel in vowels)
print(f"there overall {count} vowels in this word")

# 7 exercise
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 21, 23, 45, 43, 56, 65, 41, 76]
maxim = max(numbers) 
print(maxim)

# 8 exercise
txt = input('write a word plz')
pal = txt[::-1]

if txt == pal:
 print('it is palindrome')
else:
 print('it is not palindrome')

# 9 exercise
email = input('plz write your email address')
at = "@"
index = email.find(at)
print(email[index + 1:])

# 10 exercise
import random

len = 12
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "123456789"
special = "!@#$%^&*()-=/*-+"

all = letters + numbers + special
password = ''.join(random.choice(all) for i in range(len))
print(password)
