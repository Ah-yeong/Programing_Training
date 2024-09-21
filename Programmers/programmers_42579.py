def solution(genres, plays):
    answer = []
    dic_genres = {}
    dic_plays = {}
    
    for i in range(len(genres)):
        if genres[i] in dic_genres:
            dic_genres[genres[i]].append((i, plays[i]))
        else:
            dic_genres[genres[i]] = [(i, plays[i])]
    
        if genres[i] in dic_plays:
            dic_plays[genres[i]] += plays[i]
        else:
            dic_plays[genres[i]] = plays[i]

    sort_plays = sorted(dic_plays.items(), key = lambda item: item[1], reverse=True)
    print(sort_plays)

    for i in sort_plays:
        album = dic_genres[i[0]]
        album.sort(key = lambda x:(-x[1], x[0]))

        print(album)

        for j in range(len(album)):
            if j >= 2:
                break
            answer.append(album[j][0])

    print(answer)
    return answer

genres = ["classic", "pop", "classic", "classic", "pop", "test"]
plays = [500, 600, 150, 800, 2500, 100]

solution(genres, plays)
