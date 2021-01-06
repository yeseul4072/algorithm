def dfs(idx, s, numbers, target):
    if idx == len(numbers):
        if s == target:
            return 1
        else:
            return 0
    return dfs(idx + 1, s + numbers[idx], numbers, target) + dfs(idx + 1, s - numbers[idx], numbers, target)

def solution(numbers, target):
    return dfs(0, 0, numbers, target)