arr = list(map(int, input()))
answer = 0

for num in arr:
    if num <= 1 or answer <= 1:
        answer += num 
    else:
        answer *= num 

print(answer)