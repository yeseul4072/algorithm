def solution(n, computers):
    check = [0] * n
    cnt = 0
    for i in range(n):
        if not check[i]:
            stack = []
            stack.append(i)
            check[i] = 1
            cnt += 1
            while stack:
                x = stack.pop()
                for k in range(n):
                    if computers[x][k] == 1 and not check[k]:
                        stack.append(k)
                        check[k] = 1
    return cnt