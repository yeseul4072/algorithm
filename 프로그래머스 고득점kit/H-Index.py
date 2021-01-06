def solution(citations):
    citations.sort()
    e = len(citations)
    i = e - 1
    r = 0
    for h in range(e, -1, -1):
        while i >= 0:
            if h == citations[i]:
                if r + 1 >= h and e - (r + 1) <= h:
                    return h
                break
            elif h > citations[i]:
                if r >= h and e - r <= h:
                    return h
                break
            else:
                i -= 1
                r += 1

print(solution([1, 0, 6, 1, 5]))