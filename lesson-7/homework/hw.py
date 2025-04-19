def is_prime(num):
  if num <= 1:
    return False
  for i in range(2, int(num**0.5) +1):
    if num % i == 0:
      return False
  return True

def digit_sum(k):
  return sum(int(digit) for digit in str(k))

def in_square(n):
  k = 2
  result = []
  while k < n:
    result.append(k)
    k *= 2
  return result
