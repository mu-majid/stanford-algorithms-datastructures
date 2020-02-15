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

  num1_str = str(num_1)
  num2_str = str(num_2)

  num1_slice_index = (num_1_digits // 2)
  num2_slice_index = (num_2_digits // 2)

  # Ceiling.
  if num_1_digits % 2 != 0 and num_1_digits != 1:
    num1_slice_index += 1

  if num_2_digits % 2 != 0 and num_2_digits != 1:
    num2_slice_index += 1


  a = num1_str[0:num1_slice_index] if num1_str[0:num1_slice_index] else 0 
  b = num1_str[num1_slice_index:] if num1_str[num1_slice_index:] else 0

  c = num2_str[0:num2_slice_index] if num2_str[0:num2_slice_index] else 0
  d = num2_str[num2_slice_index:] if num2_str[num2_slice_index:] else 0

  # First Recursive Call a*c
  first_operand = karatsuba(int(a), int(c)) # ac

  # Second Recursive Call b*d
  second_operand = karatsuba(int(b), int(d)) # bd

  # Third Recursive Call (a+b) * (c+d)
  meta_third_operand = karatsuba((int(a) + int(b)), (int(c) + int(d))) # (a+b) * (c+d)

  # Gauss Trick
  third_operand = meta_third_operand - second_operand - first_operand

  # important
  n = max(num_1_digits, num_2_digits)
  nby2 = n // 2


  return ((10**(2*nby2)) * first_operand) + second_operand + ((10**nby2) * third_operand)
  

result = karatsuba(5678, 1234)
print(result)
