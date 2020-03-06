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


sorted_arr_1 = sort_and_count_inversions([1,3,5,2,4,6])
sorted_arr_2 = sort_and_count_inversions([5,4,1,8,7,2,6,3,3])
sorted_arr_3 = sort_and_count_inversions([9,7,5,8,2,8,2,8,1,85,4,2,5])
sorted_arr_4 = sort_and_count_inversions([9,8,7,6,5,4,3,2,1,0])
sorted_arr_5 = sort_and_count_inversions([5,4,1,8,7,2,6,3])
sorted_arr_6 = sort_and_count_inversions([1, 20, 6, 4, 5])


print('Sorted 1: ', sorted_arr_1[0], ' And Number Of Inversions : ', sorted_arr_1[1])
print('Sorted 2: ', sorted_arr_2[0], ' And Number Of Inversions : ', sorted_arr_2[1])
print('Sorted 3: ', sorted_arr_3[0], ' And Number Of Inversions : ', sorted_arr_3[1])
print('Sorted 4: ', sorted_arr_4[0], ' And Number Of Inversions : ', sorted_arr_4[1])
print('Sorted 5: ', sorted_arr_5[0], ' And Number Of Inversions : ', sorted_arr_5[1])
print('Sorted 6: ', sorted_arr_6[0], ' And Number Of Inversions : ', sorted_arr_6[1])





