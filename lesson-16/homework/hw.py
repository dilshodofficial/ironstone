import numpy as np

firstlist = [12.23, 13.32, 100, 36.32]
arrayed_list = np.array(firstlist)
print(arrayed_list)


matrix = np.array([
  [2,3,4],
  [5,6,7],
  [8,9,10]
])
print(matrix)

zeroes = np.zeros(10)
zeroes = np.insert(zeroes, 6, 11)
print(zeroes)

numbers = np.array(range(12, 39))
print(numbers)

converting_arrays = np.array([1, 2, 3, 4])
converted = np.astype(converting_arrays, np.float64)
print(converted)

inp = [0, 12, 45.21, 34, 99.91]
cel = np.asarray(inp)
print(f"Celsius {cel}")
feh = (9 * cel / 5 + 32)
print(f"Fahrenheit {feh}")


original_array = np.array([[10, 20, 30]])
original_array = np.append(original_array, [40, 50])
print(original_array)

arrays = np.random.randint(1, 100, size=10)
mean = np.mean(arrays)
median = np.median(arrays)
std = np.std(arrays)
print(f"The meean equals to => {mean}")
print(f"The median equals to => {median}")
print(f"The standard deviation equals to => {std}")

array = np.random.randint(1, 120, size=(10, 10))
min = np.min(array)
max = np.max(array)
print(f"The min equals to => {min}")
print(f"The max equals to => {max}")

matrix_last = np.random.random((3,3,3))
matrix_last
array_last = np.array(matrix_last)
print(array_last)
