def solution(genres, plays):
    answer = []
    database = {}
    idx_base = {}
    for idx, (gen, num) in enumerate(zip(genres, plays)):
        try:
            database[gen].append(int(num))
            idx_base[gen].append((idx, int(num)))
        except:
            database[gen] = [int(num)]
            idx_base[gen] = [(idx, int(num))]
    select_genre = sorted(database.items(), key=lambda x : sum(x[1]), reverse=True)
    sort_idx = sorted(idx_base.items(), key=lambda x : x[1], reverse=True)
    for gen, num in select_genre:
        answer.append(sorted(idx_base[gen], key=lambda x : x[1], reverse=True)[0][0])
        if len(idx_base[gen]) > 1:
            answer.append(sorted(idx_base[gen], key=lambda x : x[1], reverse=True)[1][0])

    return answer

solution(['classic', 'pop', 'classic', 'classic', 'pop'], [500, 600, 150, 800, 2500])


def solution(genres, plays):
    answer = []    
    database = {element: [] for element in set(genres)}
    for idx, (gen, num) in enumerate(zip(genres, plays)):
        database[gen].append((num, idx))
    # database = {'genre': [plays, idx], 'genre2': [plays, idx] ... }
    genre_sorted = sorted(list(database.keys()), key=lambda x : sum(map(lambda y : y[0], database[x])), reverse=True)
    
    for gen in genre_sorted:
        plays_sorted = sorted(database[gen], key=lambda x : x[0], reverse=True)
        answer.append(plays_sorted[0][1])
        if len(plays_sorted) > 1:
            answer.append(plays_sorted[1][1])           # 이 부분 줄일 수 있을 것 같은데
            
    return answer

''' 
시간복잡도
O(N LogN)
'''