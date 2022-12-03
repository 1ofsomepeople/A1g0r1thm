import random

def quicksort(arr:list, left:int, right:int):
  if left >= right:
    return
  p_idx = random.randint(left, right)
  l, r = left, right
  while l < r:
    # 此处完成一次"移动指针"或"交换pivot"操作
    if l < p_idx:
      if arr[l] < arr[p_idx]:
        l += 1
      else:
        arr[l], arr[p_idx] = arr[p_idx], arr[l]
        p_idx = l
    else:
      if arr[r] >= arr[p_idx]:
        r -= 1
      else:
        arr[r], arr[p_idx] = arr[p_idx], arr[r]
        p_idx = r
  quicksort(arr, left, p_idx)
  quicksort(arr, p_idx+1, right)

arr = random.choices(range(0, 99), k=20) 
print(arr) 
print(sorted(arr))
quicksort(arr, 0, len(arr)-1)
print(arr) 
