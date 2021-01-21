# 선택정렬
# 1. 배열을 돌며 최소값 선택해서 맨 앞에 위치한 값과 교체
# 2. 그 다음 위치에 그 다음 최소값 찾아서 교체
# 3. 1, 2 반복
# 교환은 한 번만 이루어지기에 버블 정렬보다 우위에 있다
# 시간 복잡도 : O(n^2)

def selectSort(arr):
    l = len(arr)
    for i in range(l - 1):
        min_v = arr[i]
        min_idx = i
        for j in range(i + 1, l):
            if arr[j] < min_v:
                min_v = arr[j]
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

print(selectSort([4, 3, 5, 1, 2]))