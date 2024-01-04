import sys
input = sys.stdin.readline

s = list(input())

if s[0] == '0':
    zero_cnt = 1
    one_cnt = 0
else:
    one_cnt = 1
    zero_cnt = 0

standard = s[0]

for i in range(1, len(s)):
    if s[i] != standard and s[i] == '0':
        zero_cnt += 1
        standard = s[i]
    elif s[i] != standard and s[i] == '1':
        one_cnt += 1
        standard = s[i]
            
print(min(zero_cnt, one_cnt))