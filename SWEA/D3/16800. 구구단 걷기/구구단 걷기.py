import math
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())

    key = 1
    for i in range(int(math.sqrt(n)),0,-1):
        if n % i == 0:
            key = i
            break
    key2 = n // key
    print(f"#{test_case} {(key-1)+(key2-1)}")
