"""
문제: 스택(10828번)

접근 방법 1. 각 명령어에 맞는 함수를 구현

접근 방법 2. 리스트에 데이터가 없는 경우에 대한 조건
"""

import sys

t = int(sys.stdin.readline())

def push(i):
    x.append(i)

def pop():
    if len(x) == 0:
        print('-1')
    else:
        print(x.pop(-1))

def size():
    print(len(x))

def empty():
    if not x:
        print("1")
    else:
        print("0")

def top():
    if len(x) == 0:
        print('-1')
    else:
        print(x[-1])

x = []
data = []
for i in range(t):
    data.append(sys.stdin.readline().split())

for i in range(t):

    if(data[i][0] == 'push'):
        push(int(data[i][1]))
    elif(data[i][0] == "pop"):
        pop()
    elif(data[i][0] == "size"):
        size()
    elif(data[i][0] == "empty"):
        empty()
    elif(data[i][0] == "top"):
        top()
    else:
        print("해당없음")
    
