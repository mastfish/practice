def merge(left, right):
  result = []
  while (len(left) > 0) and (len(right) > 0):
    if (left[0] >= right[0]):
      result.append(right[0])
      right = right[1:]
    else:
      result.append(left[0])
      left = left[1:]
  while (len(left) > 0):
    result.append(left[0])
    left = left[1:]
  while (len(right) > 0):
    result.append(right[0])
    right = right[1:]
  return result

def merge_sort(items):
  if (len(items) == 1):
    return items
  else:
    pivot = len(items)/2
    left = merge_sort(items[:pivot])
    right = merge_sort(items[pivot:])
    return merge(left, right)

input = [5, 6, 7, 3, 4, 3, 2, 8, 10, 12]

print merge_sort(input)
