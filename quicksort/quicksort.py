import random

def quicksort(arr:list, left:int, right:int):
  if left>=right:
    return
  p_idx = random.randint(left, right)
  l, r = left, right
  while left<right:
    # 此处完成一次"移动指针"或"交换pivot"操作
    if left<p_idx:
      if arr[left]<arr[p_idx]:
        left += 1
      else:
        arr[left], arr[p_idx] = arr[p_idx], arr[left]
        p_idx = left
    else:
      if arr[right]>=arr[p_idx]:
        right -= 1
      else:
        arr[right], arr[p_idx] = arr[p_idx], arr[right]
        p_idx = right
  quicksort(arr, l, p_idx)
  quicksort(arr, p_idx+1, r)

arr = [random.randint(0,99) for _ in range(20)]
print(arr) 
print(sorted(arr))
quicksort(arr,0,len(arr)-1)
print(arr) 
