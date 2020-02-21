"""
Implementation of Strassen's Algorithm (1969) for multiplying two matrices (square matrices)

Only Square with sizes of Power 2 (2*2, 4*4, 8*8, ... )

This Algorithm takes less than theta(n^3)

@TODO: Truncate The CEx Matrix (UnDo the padding)
"""

import numpy as np
import math

def next_pow_2(max_size):
  next_pow = math.ceil(math.log2(max_size))
  return 2 ** next_pow

def extend_matrix(mat, size, rows, cols):
  r_pad = size - rows
  c_pad = size - cols

  return np.pad(mat, ((0,r_pad), (0,c_pad)), mode='constant',constant_values=0)

def split(matrix, rows, cols):
  """Split a matrix into sub-matrices."""

  r, h = matrix.shape
  result = matrix.reshape(h // rows, rows, -1, cols).swapaxes(1, 2).reshape(-1, rows, cols)
  
  return result

def strassen(matrix_a, matrix_b):
  # Handle Base Case
  if matrix_a.shape[0] == 1 and matrix_b.shape[0] == 1:
    return np.array([matrix_a[0] * matrix_b[0]])

  a_rows, a_cols = matrix_a.shape
  b_rows, b_cols = matrix_b.shape
  # Get submatrices
  A, B, C, D = split(matrix_a, int(a_rows/2), int(a_cols/2))
  E, F, G, H = split(matrix_b, int(b_rows/2), int(b_cols/2))

  P1 = strassen(A, F - H)
  P2 = strassen(A + B, H)
  P3 = strassen(C + D, E)
  P4 = strassen(D, G - E)
  P5 = strassen(A + D, E + H)
  P6 = strassen(B - D, G + H)
  P7 = strassen(A - C, E + F)

  C11 = P5 + P4 - P2 + P6
  C12 = P1 + P2
  C21 = P3 + P4
  C22 = P1 + P5 - P3 - P7

  C = np.bmat([[C11, C12], [C21, C22]])
  return C

def execStrassen(A, B):

  a_rows, a_cols = A.shape
  b_rows, b_cols = B.shape

  if a_cols != b_rows:
    raise Exception('Dimensions Mismatch Error')

  max_size = max(a_rows, a_cols, b_rows, b_cols)
  next_power_of_2 = next_pow_2(max_size)

  AEx = extend_matrix(A, next_power_of_2, a_rows, a_cols)
  BEx = extend_matrix(B, next_power_of_2, b_rows, b_cols)
  
  CEx = strassen(AEx, BEx)

  return CEx


# Test

matrix_a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]])
matrix_b = np.array([[-1,2,3,20], [5,7,7,21], [9,0,11,13], [13,25,26,-10]])

n = np.array([[2, 1, 3], [5, 8, 7]]) # 2*3
m = np.array([[1,2], [3,4]]) # 2*2

output_1 = execStrassen(matrix_a, matrix_b)
output_2 = execStrassen(m, n)

print(output_1)
print(output_2)
