# 거품정렬(Bubble-sort)
# 1. 배열 전체를 쭉 돌며 배열에서 연속된 두 요소를 비교해서 순서가 잘못되어 있으면 두 요소를 맞바꾼다.
# 2. 한번 돌았을 때 마지막부터 부터 가장 큰 수가 정렬된다.
# 3. 1, 2번을 n번 시행하면 전체 배열이 정렬된다
# 시간 복잡도 : O(n^2)

def bubbleSort(arr):
    n = len(arr)
    cnt = 0
    for _ in range(n):
        for i in range(n - 1 - cnt):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        cnt += 1
    return arr

print(bubbleSort([4, 3, 5, 1, 2]))