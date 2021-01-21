# def solution(healths, items):
#     items = sorted([item + [i + 1] for i, item in enumerate(items)], reverse=True)
#     healths.sort()
#     ans = []
#     for item in items:
#         if healths:
#             if healths[-1] - 100 < item[1]:
#                 continue
#             for i, health in enumerate(healths):
#                 if (health - 100) >= item[1]:
#                     ans.append(item[2])
#                     del healths[i]
#                     break
#         else:
#             break
#     return sorted(ans)

import heapq

def solution(healths, items):
    items = [[item[1]] + [item[0]] + [i + 1] for i, item in enumerate(items)]
    items.sort()
    # print(items)
    len_items = len(items)
    healths.sort()
    heap = []
    ans = []
    item_idx = 0
    minus, plus, idx = 0, 1, 2
    for health in healths:
        while item_idx < len_items:
            item = items[item_idx]
            if health - item[minus] >= 100:
                heapq.heappush(heap, (-item[plus], item[idx]))
                item_idx += 1
            else:
                break
        if len(heap):
            power, i = heapq.heappop(heap)
            ans.append(i)

    return sorted(ans)

print(solution([200, 120, 150], [[30,100],[500,30],[100,400]]))

import heapq

def solution(healths, items):
    items = [[item[1]] + [item[0]] + [i] for i, item in enumerate(items, 1)]
    items.sort()
    # print(items)
    len_items = len(items)
    healths.sort()
    heap = []
    ans = []
    item_idx = 0
    HEALTH, ATTAK, IDX = 0, 1, 2
    for health in healths:
        while item_idx < len_items:
            item = items[item_idx]
            if health - item[HEALTH] < 100:
                break
            heapq.heappush(heap, (-item[ATTAK], item[IDX]))
            item_idx += 1
        if heap:
            power, i = heapq.heappop(heap)
            ans.append(i)

    return sorted(ans)