def merge_sort (array_to_sort) :

  if len(array_to_sort) <= 1:
    return array_to_sort

  output_array = [None] * len(array_to_sort)
  mid = len(array_to_sort) // 2
 
  lhs = merge_sort(array_to_sort[:mid])
  rhs = merge_sort(array_to_sort[mid:])

  lhs_iter = 0
  rhs_iter = 0
  out_iter = 0

  while (lhs_iter<len(lhs) and rhs_iter<len(rhs)):

    if(lhs[lhs_iter]<rhs[rhs_iter]):
      output_array[out_iter] = lhs[lhs_iter]
      lhs_iter = lhs_iter+1
    else:
      output_array[out_iter] = rhs[rhs_iter]
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


  return output_array



sorted_arr_1 = merge_sort([5,4,1,8,7,2,6,3])
sorted_arr_2 = merge_sort([5,4,1,8,7,2,6,3,3])
sorted_arr_3 = merge_sort([9,7,5,8,2,8,2,8,1,85,4,2,5])
sorted_arr_4 = merge_sort([9,8,7,6,5,4,3,2,1,0])


print('Sorted 1: ', sorted_arr_1)
print('Sorted 2: ', sorted_arr_2)
print('Sorted 3: ', sorted_arr_3)
print('Sorted 4: ', sorted_arr_4)


