# 1. 속한 노래가 많이 재생된 장르 먼저 수록
# 2. 장르 내에서 많이 재생된 노래 먼저 수록
# 3. 장르 내에서 재생 횟수가 같은 노래는 고유 번호가 낮은 노래를 먼저 수록
def solution(genres, plays):
    answer = []
    most_genres = dict()
    play_lists = dict()
    num_plays = []
    for i, p in enumerate(plays):
        num_plays.append((i, p))
        
    for genre, play in zip(genres, num_plays):
        if genre in most_genres:
            most_genres[genre] += play[1]
            play_lists[genre].append(play)
        else:
            most_genres[genre] = play[1]
            play_lists[genre] = [play]
    
    # 속한 노래가 많이 재생된 장르 수록
    sorted_genres = []
    for k, v in most_genres.items():
        sorted_genres.append((k, v))
    sorted_genres.sort(key = lambda x : -x[1])
    
    # 장르 내에서 많이 재생된 노래 먼저 수록
    for genre, num_plays in sorted_genres:
        play_list = play_lists[genre]
        sorted_play_list = sorted(play_list, key=lambda x : (-x[1], x[0]))
        sorted_play_list = sorted_play_list[:2]
        for a, b in sorted_play_list:
            answer.append(a)
            
    return answer