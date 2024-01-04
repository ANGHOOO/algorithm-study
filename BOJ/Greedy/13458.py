import sys
input = sys.stdin.readline

N = int(input())
students = list(map(int, input().split()))
left_students = []
head_director, sub_director = map(int, input().split())

answer = len(students)

for student in students:
    left_students.append(student - head_director)
    
for student in left_students:
    if student <= 0:
        pass
    elif student > sub_director:
        div, mod = student // sub_director, student % sub_director
        if mod > 0:
            answer += (div + 1)
        else:
            answer += div
    else:
        answer += 1
    
print(answer)