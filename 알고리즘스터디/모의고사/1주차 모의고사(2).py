from collections import deque

def solution(m, n, infests, vaccinateds):
    check = [[False] * n for _ in range(m)]
    for vac in vaccinateds:
        check[vac[0] - 1][vac[1] - 1] = True
    deq = []
    for infest in infests:
        r = infest[0] - 1
        c = infest[1] - 1
        check[r][c] = True
        deq.append([r, c, 0])
    deq = deque(deq)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while deq:
        r, c, day = deq.popleft()
        for x, y in zip(dx, dy):
            if 0 <= r + x < m and 0 <= c + y < n:
                if not check[r + x][c + y]:
                    check[r + x][c + y] = True
                    deq.append([r + x, c + y, day + 1])
    return day

print(solution(2, 4, [[1,4],[2,2]], [[1,2]]))