"""
Based On the Partition subroutine discussed in the quick sort algorithm.

Also this algorithm is A Randomized Algorithm.
"""

import random

def partition (arr, start, end):
  pivot_index = random.randrange(start,end)
  pivot = arr[pivot_index]
  arr[pivot_index], arr[start] = arr[start], arr[pivot_index] # place the pivot at the beginning
  i = start + 1
  for j in range(start+1,end+1):
   if arr[j] < pivot:
     arr[i], arr[j] = arr[j], arr[i]
     i += 1
  arr[start], arr[i-1] = arr[i-1], arr[start]
  return i-1

def r_select(array, length, stat_order):
  if length == 1:
    return array[0]

  split = partition(array, 0, len(array)-1)
  if split == stat_order:
    return array[split]

  elif split > stat_order:
    return r_select(array[:split], len(array[:split]), stat_order)

  elif split < stat_order:
    return r_select(array[split+1:], len(array[split+1:]) , stat_order - (split+1))


print('test-1 : ', r_select([10, 8, 2, 4],4, 2)) # 8
print('test-2 : ', r_select([7, 10, 4, 3, 20, 15],6, 2)) # 7
print('test-3 : ', r_select([12, 3, 5, 7, 4, 19, 26],7, 2)) # 5


