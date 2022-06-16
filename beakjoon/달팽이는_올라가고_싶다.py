"""
문제: 달팽이는 올라가고 싶다(2869번)

접근 방식 1. 반복문을 쓰면 안됨
- 반복문을 쓰지 않고 계산식을 사용
- a와 b 차이 값의 몫을 구해서 day를 구함

접근 방식 2. 나머지가 생기는 경우를 고려
- 딱 떨어지지 않을 경우 +1이 필요

접근 방식 3. 마지막에 내려오지 않고 다 올라가는 경우
- a가 100인데 차이는 1인 경우에 대한 처리가 필요
"""

import sys
a, b, v = map(int, sys.stdin.readline().split())

day = (v-a) // (a-b) + 1
if ((v-a) % (a-b) > 0):
    day = day + 1

sys.stdout.write(str(day))