import sys
input = sys.stdin.readline

N = int(input())
meetings = [tuple(map(int, input().split())) for _ in range(N)]

def max_meetings(meetings):
    sorted_meetings = sorted(meetings, key = lambda x : (x[1], x[0]))
    count = 0
    end_time = 0
    
    for st, et in sorted_meetings:
        if st >= end_time:
            count += 1
            end_time = et
            
    return count

result = max_meetings(meetings)
print(result)  