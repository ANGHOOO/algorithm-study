import sys
input = sys.stdin.readline
num = int(input())
org = num
cycle = 0

while True:
    a, b = num // 10, num % 10
    temp = a + b
    num = b * 10 + (temp % 10)
    cycle += 1
    
    if num == org:
        print(cycle)
        break