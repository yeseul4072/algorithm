import heapq


def solution(jobs):
    n = len(jobs)
    cnt = 0
    time = 0 # 현재 시점
    ans = 0
    heap = []
    jobs = sorted(jobs, key=lambda x: (x[0], x[1]))
    while cnt < n:
        for job in jobs:
            if job[0] < time:
                heapq.heappush(heap, (job[1], job[0]))
        if len(heap):
            t, s = heapq.heappop(heap)
            ans += time - s + t
            time += t
        else:
            job = jobs.pop(0)
            ans += job[1]
            time = job[0] + job[1]
        cnt += 1
    return ans // n




