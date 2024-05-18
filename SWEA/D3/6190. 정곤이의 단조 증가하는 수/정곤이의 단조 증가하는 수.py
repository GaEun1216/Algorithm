T = int(input())
result = []
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int,input().split()))
    brr = []
    max_ans = -1

    for i in range(N-1):
        for j in range(i+1,N):
            brr.append(arr[i]*arr[j])
    brr.sort(reverse=True)
    for i in range(len(brr)):
        number = brr[i]
        temp = []
        while number > 0:
            temp.append(number%10)
            number //= 10
        if temp == sorted(temp,reverse=True):
            max_ans = brr[i]
            break
    result.append(max_ans)


for test_case in range(1, T + 1):
    print(f'#{test_case} {result[test_case - 1]}')