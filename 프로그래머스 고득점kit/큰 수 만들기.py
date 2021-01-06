def solution(number, k):
    stack = []
    i = 0
    while k > 0:
        if stack:
            if stack[-1] < number[i]:
                while k > 0 and stack:
                    if stack[-1] < number[i]:
                        stack.pop()
                        k -= 1
                    else:
                        break
        stack.append(number[i])
        i += 1
    if i < len(number) - 1:
        return ''.join(stack) + number[i:]
    return ''.join(stack)

print(solution('10000', 2))