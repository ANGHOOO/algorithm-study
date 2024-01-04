import sys
input = sys.stdin.readline

splits = input().split('-')
result = sum(list(map(int, splits[0].split('+'))))

for i in range(1, len(splits)):
    result -= sum(list(map(int, splits[i].split('+'))))
    
print(result)