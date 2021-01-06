# 첫 번째 풀이
def solution(skill, skill_trees):
    d = {}
    cnt = 0
    for i, char in enumerate(skill):
        d[char] = i
    l = len(skill)
    for skill_tree in skill_trees:
        temp = []
        for s in skill_tree:
            if s in skill:
                temp.append(d[s])
        if temp == list(range(len(temp))):
            cnt += 1
    return cnt

# 두 번째 풀이
# temp에 저장하지 않고 바로 비교하면 더 빠르다
def solution(skill, skill_trees):
    d = {}
    cnt = 0
    for i, char in enumerate(skill):
        d[char] = i
    l = len(skill)
    for skill_tree in skill_trees:
        cur_idx = 0
        for s in skill_tree:
            if s in skill:
                if d[s] == cur_idx:
                    cur_idx += 1
                else:
                    break
        else:
            cnt += 1
    return cnt
