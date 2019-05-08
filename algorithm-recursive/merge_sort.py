array = [9,5,2,8,4,7,1,3,6,10]

print(array)

def merge_sort(left,right):
  print(str(left) + ', ' + str(right))
  if left >= right:
    return
  mid = int((left + right) / 2)
  merge_sort(left, mid)
  merge_sort(mid + 1, right)
  left_index = left
  right_index = mid + 1
  temp_array = []
  while left_index <= mid or right_index <= right:
    if left_index > mid:
      temp_array.append(array[right_index])
      right_index += 1
    elif right_index > right:
      temp_array.append(array[left_index])
      left_index += 1
    elif array[right_index] < array[left_index]:
      temp_array.append(array[right_index])
      right_index += 1
    else:
      temp_array.append(array[left_index])
      left_index += 1

  temp_index = 0

  for i in range(left, right + 1):
    array[i] = temp_array[temp_index]
    temp_index += 1

merge_sort(0, 9)

print(array)
