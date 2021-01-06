def choice(arr):
    res = []
    if len(arr) < 2:
        res.append(arr[0][1])
        return res
    for i in range(2):
        max_play = 0
        max_idx = -1
        for play, idx in arr:
            if play > max_play:
                max_play = play
                max_idx = idx
            elif play == max_play and max_idx > idx:
                max_idx = idx
        res.append(max_idx)
        del arr[max_idx]
    return res


def solution(genres, plays):
    # 장르를 키로, 재생 횟수의 합을 값으로 가지는 딕셔너리 => sum_genre
    # 장르를 키로, 재생 횟수와 고유번호를 값으로 가지는 딕셔너리 => dic_genre
    sum_genre = {}
    dic_genre = {}
    for i in range(len(genres)):
        g = genres[i]
        p = plays[i]
        if g in sum_genre:
            sum_genre[g] += p
        else:
            sum_genre[g] = p
        if g in dic_genre:
            dic_genre[g].append((p, i))
        else:
            dic_genre[g] = [(p, i)]
    print(sum_genre)
    print(dic_genre)
    # 재생 횟수를 기준으로 장르 내림차순 정렬
    st_genre = sorted(sum_genre, key=lambda x: sum_genre[x], reverse=True)
    print(st_genre)
    # 정렬한 장르 반복 => dic에서 값의 재생 횟수를 기준으로 가장 큰 두 값 조회
    ans = []
    for g in st_genre:
        ans += choice(dic_genre[g])
    return ans

print(solution(['classic', 'pop', 'classic', 'classic', 'pop'], [500, 600, 150, 800, 2500]))


def solution(genres, plays):
    answer = []
    d = {e:[] for e in set(genres)}
    for e in zip(genres, plays, range(len(plays))):
        d[e[0]].append([e[1] , e[2]])
    genreSort =sorted(list(d.keys()), key= lambda x: sum( map(lambda y: y[0],d[x])), reverse = True)
    for g in genreSort:
        temp = [e[1] for e in sorted(d[g],key= lambda x: (x[0], -x[1]), reverse = True)]
        answer += temp[:min(len(temp),2)]
    return answer