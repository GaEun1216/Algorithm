T = 10 #int(input())

for test_case in range(1, T + 1):

    case = int(input())
    arr = [ list(map(int,input().split())) for _ in range(100) ]
    brr = list(zip(*arr))
    result = 0
    for i in range(100):
        result = max(sum(arr[i]),sum(brr[i]),result)
    answer1 = 0
    answer2 = 0
    for i in range(100):
        answer1 += arr[i][i]
        answer2 += arr[i][99-i]
    result = max(answer1,answer2,result)
    print(f"#{case} {result}")


