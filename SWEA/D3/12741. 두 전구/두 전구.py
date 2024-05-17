
T = int(input())
answer = []
for test_case in range(1, T + 1):
    A,B,C,D = map(int,input().split())
    result = min(B,D) - max(A, C)
    if result < 0:
        result = 0
    answer.append(result)
for test_case in range(1, T + 1):
    print(f"#{test_case} {answer[test_case-1]}")


