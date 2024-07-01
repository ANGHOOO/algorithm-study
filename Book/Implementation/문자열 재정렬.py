arr = list(input())
alpha = []
num = []

for a in arr:
    if a.isalpha():
        alpha.append(a)
    else:
        num.append(a)

alpha.sort()
num_sum = 0
for n in num:
    num_sum += int(n)

result = ''
result = result.join(alpha) + str(num_sum)
print(result)