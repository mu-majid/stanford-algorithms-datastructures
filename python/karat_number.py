"""
@author: mu-majid

Implementation Of Karatsuba Multiplication Algorithm
With 3 Recursive Calls

Date: 31/1/2020

"""

import math


def number_of_digits(number):
  """
  Used log10 to find no. of digits
  """
  if number > 0:
    return int(math.log10(number)) + 1
  elif number == 0:
    return 1
  else:
    return int(math.log10(-number)) + 1 # Don't count the '-'

def karatsuba(num_1, num_2):

  num_1_digits = number_of_digits(num_1)
  num_2_digits = number_of_digits(num_2)

  # Base Case
  if num_1_digits == 1 and num_2_digits == 1:
    return num_1 * num_2

  n = max(num_1_digits, num_2_digits)
  nby2 = n // 2 # slicing index

  a = num_1 // 10**nby2
  b = num_1 % 10**nby2

  c = num_2 // 10**nby2
  d = num_2 % 10**nby2

  # First Recursive Call a*c
  first_operand = karatsuba(a, c) # ac

  # Second Recursive Call b*d
  second_operand = karatsuba(b, d) # bd

  # Third Recursive Call (a+b) * (c+d)
  meta_third_operand = karatsuba((a + b), (c + d)) # (a+b) * (c+d)

  # Gauss Trick
  third_operand = meta_third_operand - second_operand - first_operand

  return ((10**(2*nby2)) * first_operand) + second_operand + ((10**nby2) * third_operand)
  
  

result = karatsuba(134, 46)
print(result)
