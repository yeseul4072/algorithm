# 병합정렬(분할정복)
# 배열을 더이상 쪼갤 수 없을 때까지 쪼갠 후 정렬하며 합쳐(정복)나가는 정렬 방식
# 시간복잡도 O(nlogn)

def mergeSort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    left = mergeSort(left)
    right = mergeSort(right)
    return merge(left, right)

# 두 개의 정렬된 배열을 하나의 정렬된 배열로 합쳐서 반환
def merge(left, right):
    left_idx = right_idx = 0
    res = []
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] <= right[right_idx]:
            res.append(left[left_idx])
            left_idx += 1
        else:
            res.append(right[right_idx])
            right_idx += 1
    if left_idx < len(left):
        res += left[left_idx:]
    if right_idx < len(right):
        res += right[right_idx:]
    return res

print(mergeSort([6,4,3,8,7,2,9,1,10]))