from collections import deque
import heapq

def solution(reqs):
    # cur_time = 1
    # heap = []
    # reqs = [req + [i] for i, req in enumerate(reqs, 1)]
    # reqs = deque(reqs[1:])
    # rank, time = reqs[0][0], reqs[0][1]
    # ans = [1]
    # while len(reqs):
    #     if not cur_time % 3:
    #         temp_r, temp_t, order = reqs.popleft()
    #         heapq.heappush(heap, (-temp_r, temp_t, order))
    #     if cur_time == time and len(heap):
    #         r, t, o = heapq.heappop(heap)
    #         time += t
    #         ans.append(o)
    #     cur_time += 1
    # return ans
    reqs = [req + [i] for i, req in enumerate(reqs, 1)]
    reqs = deque(reqs)
    waiting = []
    cur_time, time = 0, 0
    ans = []
    cnt = 0
    l = len(reqs)
    while cnt < l:
        if not cur_time % 3:
            temp_r, temp_t, idx = reqs.popleft()
            heapq.heappush(waiting, (-temp_r, temp_t, idx))
        if time == cur_time:
            r, t, i = heapq.heappop(waiting)
            time += t
            ans.append(i)
            cnt += 1
        cur_time += 1
    return ans

print(solution([[1, 7], [3, 2], [4, 1], [5, 2]]))



