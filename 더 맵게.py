import heapq

def solution(scoville, k):
    cnt = 0
    while True:
        n1 = heapq.heappop(scoville)
        if n1 >= k:
            return cnt
        if not scoville:
            return -1
        n2 = heapq.heappop(scoville)
        heapq.heappush(scoville, n1 + n2 * 2)
        cnt += 1

print(solution([1, 2, 3, 9, 10, 12], 7))