from IPython import embed

def merge(left, right):
  result = []
  while (len(left) > 0) and (len(right) > 0):
    if left[0] <= right[0]
    embed()

def merge_sort(items):
  if (len(items) == 1):
    return items
  else:
    pivot = len(items)/2
    left = merge_sort(items[:pivot])
    right = merge_sort(items[pivot:])
    return merge(left, right)

input = [5, 6, 7, 3, 4, 3, 2, 8, 10, 12]

merge_sort(input)
