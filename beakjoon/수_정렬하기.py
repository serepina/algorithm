"""
문제: 수 정렬하기(2750번)

접근 방법 1. 입력 데이터의 중복을 제거한다.

접근 방법 2. 데이터를 정렬한다.
"""

import sys

t = int(sys.stdin.readline())

li = []
for i in range(t):
    li.append(int(sys.stdin.readline()))

result = list(set(li))
result.sort()

for i in result:
    print(i)
