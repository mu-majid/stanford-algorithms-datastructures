"""
This file contains all of the 100,000 integers between 1 and 100,000 (inclusive) in some order, with no integer repeated.
Your task is to compute the number of inversions in the file given, where the  row of the file indicates the  entry of an array.
Because of the large size of this array, you should implement the fast divide-and-conquer algorithm covered in the video lectures.
The numeric answer for the given input file should be typed in the space below.
So if your answer is 1198233847, then just type 1198233847 in the space provided without any spaces or commas or any other punctuation marks. You can make up to 5 attempts.
(We do not require you to submit your code, so feel free to use any programming language you want --- just type the final numeric answer in the following space.)
[TIP: before submitting, first test the correctness of your program on some small test files or your own devising. Then post your best test cases to the discussion forums to help your fellow students!]
"""

def sort_and_count_inversions (array_to_sort) :

  split_inversions = 0

  if len(array_to_sort) <= 1:
    return [array_to_sort, 0]

  output_array = [None] * len(array_to_sort)
  mid = len(array_to_sort) // 2
 
  [lhs, lhs_inversions] = sort_and_count_inversions(array_to_sort[:mid])
  [rhs, rhs_inversions] = sort_and_count_inversions(array_to_sort[mid:])

  lhs_iter = 0
  rhs_iter = 0
  out_iter = 0

  while (lhs_iter<len(lhs) and rhs_iter<len(rhs)):

    if(lhs[lhs_iter] <= rhs[rhs_iter]):
      output_array[out_iter] = lhs[lhs_iter]
      lhs_iter = lhs_iter+1
    else:
      output_array[out_iter] = rhs[rhs_iter]
      # key idea is here
      split_inversions += (len(lhs) - lhs_iter)
      rhs_iter = rhs_iter+1
    
    out_iter = out_iter + 1

  # Handle array lengths are not equal
  while(lhs_iter < len(lhs)):

    output_array[out_iter] = lhs[lhs_iter]
    lhs_iter = lhs_iter + 1
    out_iter = out_iter + 1

  while(rhs_iter < len(rhs)):

    output_array[out_iter] = rhs[rhs_iter]
    rhs_iter = rhs_iter + 1
    out_iter = out_iter + 1

  return [output_array, (lhs_inversions + rhs_inversions + split_inversions)]



unsorted_list = [int(x) for x in open("./input.txt", "r").read().splitlines()]

# efficient inversion count
sortedArr, inversions = sort_and_count_inversions(unsorted_list)
print(f" Inversions: {inversions}")

assert inversions == 2407905288