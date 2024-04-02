# my solution
n = int(input())

answer = 0

total_time = n * 60 * 60 + 59 * 60 + 59

for t in range(total_time+1):
    hour = t // (60 * 60)
    t = t % (60 * 60)
    minute = t // 60
    t = t % 60
    second = t % 60
    if '3' in str(hour) or '3' in str(minute) or '3' in str(second):
        answer += 1

print(answer)

# book solution
h = int(input())
answer = 0

for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                answer += 1

print(answer)