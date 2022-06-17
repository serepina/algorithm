"""
문제: ACM 호텔

접근 방법 1. 세로로 밑에서부터 채운다.

접근 방법 2. 나머지가 0인 경우를 고려해야한다.
"""
import sys

t = int(input())

li = []
for i in range(t):
    li.append(list(map(int, sys.stdin.readline().split())))

for j in range(t):
    quo = (li[j][2] // li[j][0])
    rest = li[j][2] % li[j][0]
    if rest == 0:
        rest = li[j][0]
    else:
        quo = quo + 1
    print(int(str(rest)+str(quo).zfill(2)))