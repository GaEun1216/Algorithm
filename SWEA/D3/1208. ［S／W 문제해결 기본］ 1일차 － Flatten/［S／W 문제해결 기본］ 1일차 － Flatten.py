from collections import deque

T = 10

for tc in range(1, T + 1):
    count = int(input())
    number = list(map(int,(input().split())))
    for i in range(count):
        number.sort()
        number[0] += 1
        number[99] -= 1
    number.sort()
    result = number[99] - number[0]
    print(f"#{tc} {result}")
