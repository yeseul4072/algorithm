min_cnt = 50

def check(w1, w2):
    cnt = 0
    for i in range(len(w1)):
        if w1[i] == w2[i]:
            cnt += 1
    if cnt == len(w1) - 1:
        return True
    else:
        return False

def bfs(word, words, cnt, visit, target):
    global min_cnt
    if word == target:
        min_cnt = min(cnt, min_cnt)
        return
    for i, w in enumerate(words):
        if not visit[i] and check(word, w):
            visit[i] = 1
            bfs(w, words, cnt + 1, visit, target)
            visit[i] = 0

def solution(begin, target, words):
    if target not in words:
        return 0
    else:
        visit = [0] * len(words)
        bfs(begin, words, 0, visit, target)
        return min_cnt