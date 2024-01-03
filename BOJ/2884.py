import sys
input = sys.stdin.readline
hour, minute = map(int, input().split())

if minute < 45:
    if hour == 0:
        print(23, minute + 60 - 45)
    else:
        print(hour - 1, minute + 60 - 45)
else:
    print(hour, minute - 45)