
T = 10 #int(input())

for test_case in range(1, T + 1):
    case = int(input())
    A,B = map(int,input().split())
    print(f'#{case} {A**B}')