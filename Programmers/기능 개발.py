def solution(progresses, speeds):
    answer = []
    days = 1
    count = 0
    while progresses:
        progress, speed = progresses[0], speeds[0]
        if progress + speed * days >= 100:
            count += 1
            progresses.pop(0)
            speeds.pop(0)
        else:
            days += 1
            if count > 0:
                answer.append(count)
            count = 0
    
    answer.append(count)
    return answer