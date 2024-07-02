def possible(answer):
    for x, y, stuff in answer:
        if stuff == 0: # 기둥
            # 기둥의 y좌표가 0, 기둥의 좌표가 보의 양쪽 끝과 일치하는지, 기둥 아래에 바로 기둥이 있는지
            if y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer: # 보 : (1, 1) 기둥 : (2, 1)
                continue
            return False
            
        if stuff == 1: # 보
            # 보의 양쪽 끝 좌표가 기둥 대가리와 일치하는지, 설치하려는 보의 양 옆으로 또 다른 보가 존재하는지
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                continue # 보 : (2, 2) 기둥 : (2, 1)
            return False
    return True

def solution(n, build_frame):
    answer = []
    
    for x, y, stuff, operation in build_frame:
        if operation == 0: # 삭제
            answer.remove([x, y, stuff])
            if not possible(answer):
                answer.append([x, y, stuff])
        
        if operation == 1: # 설치
            answer.append([x, y, stuff])
            if not possible(answer):
                answer.remove([x, y, stuff])
                
    return sorted(answer)