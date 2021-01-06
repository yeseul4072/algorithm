import heapq

# 첫 번째 풀이
def solution(no, works):
    if sum(works) <= no:
        return 0
    works = [(-i, i) for i in works]
    heapq.heapify(works)
    for _ in range(no):
        x = heapq.heappop(works)[1] - 1
        heapq.heappush(works, (-x, x))
    return sum(map(lambda x: x[1]**2, works))

# 두 번째 풀이
# 제곱값을 구해주기 때문에 -값만 필요하다
def solution(no, works):
    if sum(works) <= no:
        return 0
    works = [-i for i in works]
    heapq.heapify(works)
    for _ in range(no):
        x = heapq.heappop(works) + 1
        heapq.heappush(works, x)
    return sum(map(lambda x: x**2, works))