n = 5

minute = 59
second = 59
count = 0

for i in range(n+1):
    for j in range(minute+1):
        for k in range(second+1):
            if '3' in str(i) or '3' in str(j) or '3' in str(k):
                count += 1

print(count)