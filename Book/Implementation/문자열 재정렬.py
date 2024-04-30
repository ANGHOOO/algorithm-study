arr = list(input())
alpha = []
num = []

for s in arr:
    if s.isalpha():
        alpha.append(s)
    else:
        num.append(int(s))

alpha.sort()
num = list(str(sum(num)))

answer = alpha + num 
answer = ''.join(answer)

print(answer)