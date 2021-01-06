from collections import deque

def solution(n, m, images):
    visit = [[0] * m for _ in range(n)]
    cnt = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(n):
        for j in range(m):
            if not visit[i][j]:
                deq = deque([(i, j)])
                visit[i][j] = 1
                while deq:
                    r, c = deq.popleft()
                    v = images[r][c]
                    for k in range(4):
                        a = r + dx[k]
                        b = c + dy[k]
                        if 0 <= a < n and 0 <= b < m:
                            if not visit[a][b] and images[a][b] == v:
                                deq.append((a, b))
                                visit[a][b] = 1
                cnt += 1
    return cnt