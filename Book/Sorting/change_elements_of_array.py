n, k = 5, 3
a = [1, 2, 5, 4, 3]
b = [5, 5, 6, 6, 5]

sorted_a = sorted(a)
sorted_b = sorted(b, reverse=True)

for i in range(k):
    sorted_a[i] = sorted_b[i]

print(sum(sorted_a))
