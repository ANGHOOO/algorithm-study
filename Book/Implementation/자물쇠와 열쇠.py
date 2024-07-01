def rotation90(matrix):
    n = len(matrix)
    m = len(matrix[0])
    
    new_matrix = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            new_matrix[j][n - i - 1] = matrix[i][j]
            
    return new_matrix

def check(new_lock):
    length = len(new_lock) // 3
    for i in range(length, length * 2):
        for j in range(length, length * 2):
            if new_lock[i][j] != 1:
                # print('false')
                return False
            
    return True

def solution(key, lock):
    n = len(lock)
    m = len(key)
    
    # 새로운 자물쇠 생성하고 새로운 자물쇠의 중앙에 원래 자물쇠 배치
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]
    for i in range(n):
        for j in range(n):
            new_lock[i + n][j + n] = lock[i][j]
    
    for rotation in range(4):
        key = rotation90(key)
        for x in range(n * 2):
            for y in range(n * 2):
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] += key[i][j]
                        
                if check(new_lock):
                    return True
                
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] -= key[i][j]
                
    return False