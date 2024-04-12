n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

answer = 0

for x, y in zip(a, b):
    if k > 0:
        answer += y 
        k -= 1
    else:
        answer += x 

print(answer)
