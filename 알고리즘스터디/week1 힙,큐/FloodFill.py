from collections import deque

def solution(n, m, images):
    visit = [[False] * m for _ in range(n)]
    cnt = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(n):
        for j in range(m):
            if not visit[i][j]:
                deq = deque([(i, j)])
                visit[i][j] = True
                while deq:
                    r, c = deq.popleft()
                    color = images[r][c]
                    for x, y in zip(dx, dy):
                        next_x = r + x
                        next_y = c + y
                        if 0 <= next_x < n and 0 <= next_y < m:
                            if not visit[next_x][next_y] and images[next_x][next_y] == color:
                                deq.append((next_x, next_y))
                                visit[next_x][next_y] = True
                cnt += 1
    return cnt