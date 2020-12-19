from collections import deque


def solution(skill, skill_trees):
    cnt = 0
    for skill_tree in skill_trees:
        arr = deque(skill)
        # print(arr)
        for char in skill_tree:
            if char in skill:
                if char != arr.popleft():
                    break
        else:
            cnt += 1
    return cnt


# def solution(skill, skill_trees):
#     dic = {}
#     cnt = 0
#     for idx, char in enumerate(skill):
#         dic[char] = idx
#     for skill_tree in skill_trees:
#         idx = []
#         for char in skill_tree:
#             if char in skill:
#                 idx.append(dic[char])
#         if idx == list(range(len(idx))):
#             cnt += 1
#     return cnt


print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))