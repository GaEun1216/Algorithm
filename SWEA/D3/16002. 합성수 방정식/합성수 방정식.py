T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # 말이 어렵지 그냥 합성수 * x - 합성수 * y = N이면 됨
    n = int(input())
    x = 9*n
    y = 8*n
    print(f"#{test_case} {x} {y}")
