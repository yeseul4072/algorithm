import math

# 일자를 계산해서 이전 기능의 일자보다 적게 걸리면 count 해준다
# 많이 걸리면 이전 기능들 count 값 ans에 넣고, count와 일자 값 갱신해준다
# 시간복잡도 O(N)
def solution(progresses, speeds):
    ans = []
    cnt = 0
    for progress, speed in zip(progresses, speeds):
        period = math.ceil((100 - progress) / speed)
        if cnt == 0:
            prev = period
            cnt += 1
        elif period <= prev:
            cnt += 1
        else:
            ans.append(cnt)
            cnt = 1
            prev = period
    return ans + [cnt]