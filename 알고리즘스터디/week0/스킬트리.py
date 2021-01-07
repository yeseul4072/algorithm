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

# 다영님 풀이 참고
def solution(skill, skill_trees):
    cnt = 0
    for skill_tree in skill_trees:
        cur_idx = 0
        for char in skill_tree:
            if char in skill:
                if skill[cur_idx] != char:
                    break
                cur_idx += 1
        else:
            cnt += 1
    return cnt


# filter(), startswith() 사용하기
def solution(skill, skill_trees):
    cnt = 0
    for skill_tree in skill_trees:
        impt_skill = ''.join(list(filter(lambda x: x in skill, skill_tree)))
        if skill.startswith(impt_skill):
            cnt += 1
    return cnt

