def solution(numbers):
    ans = ''
    l = len(''.join(list(map(str, numbers))))
    while len(ans) < l:
        s = -1
        check = [0] * len(numbers)
        idx = -1
        for i, number in enumerate(numbers):
            if not check[i]:
                if not (max(number, s) // min(number,s)) % 10:
                    s = min(number, s)
                    idx = i
                else:
                    temp = []
                    temp.append(str(s))
                    temp.append(str(number))
                    arr = sorted(temp, reverse=True)
                    s = int(arr[0])
                    idx = i
        check[idx] = 1
        ans += str(s)
        s = -1
    print(ans)
print(solution([6, 10, 2]))