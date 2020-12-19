from itertools import permutations

def solution(n):
    s = set()
    for i in range(len(n)):
        s |= set(map(int, map(''.join, set(permutations(n, i + 1)))))

    s -= set(range(2))
    for i in range(2, int(max(s) ** 0.5) + 1):
        s -= set(range(i, max(s) + 1, i))
    return len(s)

print(solution("011"))