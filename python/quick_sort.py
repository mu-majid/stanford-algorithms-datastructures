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

def partition2(array, start, end):
  pivot = array[start]
  low = start + 1
  high = end

  while True:
    # If the current value we're looking at is larger than the pivot
    # it's in the right place (right side of pivot) and we can move left,
    # to the next element.
    # We also need to make sure we haven't surpassed the low pointer, since that
    # indicates we have already moved all the elements to their correct side of the pivot
    while low <= high and array[high] >= pivot:
        high = high - 1

    # Opposite process of the one above
    while low <= high and array[low] <= pivot:
        low = low + 1

    # We either found a value for both high and low that is out of order
    # or low is higher than high, in which case we exit the loop
    if low <= high:
      array[low], array[high] = array[high], array[low]
      # The loop continues
    else:
      # We exit out of the loop
      break

  array[start], array[high] = array[high], array[start]

  return high


def quick_sort(array, start, end):
	if start < end:
		split = partition(array, start, end)
		quick_sort(array, start, split-1)
		quick_sort(array, split+1, end)
	return array


print('test-1 ', quick_sort([10, 7, 8, 9, 1, 5], 0, 5))
print('test-2 ', quick_sort([8, 9, 8, 8, 1], 0, 4))
print('test-3 ', quick_sort([1, 2, 3, 4, 5], 0, 4))
print('test-4 ', quick_sort([85, 60, 55, 32, 10, 8], 0, 5))

