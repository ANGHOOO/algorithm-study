from itertools import permutations, combinations
import sys 

n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

def cleaning(homes):
    distance = [[0] * (n+1) for _ in range(n+1)]
    for home in homes:
        x, y = home[0], home[1]
        distance[x][y] = 9999999

    return distance

def find_location():
    homes = []
    chickens = []

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                homes.append((i, j))
            if arr[i][j] == 2:
                chickens.append((i, j))

    return homes, chickens

def check_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

# 1. 모든 치킨집 중에서 m개 만큼의 치킨집을 남기는 조합 생성
# 2. 해당 조합으로 남겨진 치킨집에 대해 모든 집과의 거리 계산
# 3. 전체 조합에 대해 계산 한 거리 중 가장 작은 거리를 정답으로 도출

def simulate():
    homes, chickens = find_location()
    chicken_candidates = list(combinations(chickens, m))
    results = []
    distance = cleaning(homes)

    for chicken in chicken_candidates:
        distance = cleaning(homes)
        for c in chicken:
            x1, y1 = c 

            for home in homes:
                x2, y2 = home[0], home[1]
                diff = check_distance(x1, y1, x2, y2)
                diff = min(distance[x2][y2], diff)
                distance[x2][y2] = diff

        temp = 0
        for i in range(n+1):
            for j in range(n+1):
                temp += distance[i][j]

        results.append(temp)

    return min(results)

print(simulate())
