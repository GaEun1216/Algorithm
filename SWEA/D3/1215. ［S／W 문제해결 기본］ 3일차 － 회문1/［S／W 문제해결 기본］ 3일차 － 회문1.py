T = 10 #int(input())

for test_case in range(1, T + 1):

    length = int(input())
    arr = [ list(input()) for _ in range(8) ]
    brr = list(zip(*arr))
    result = 0
    for i in range(8):
        for j in range(8-length+1):
            
            tmp1 = arr[i][j:j+length]
            tmp2 = brr[i][j:j+length]
            if tmp1 == tmp1[::-1]:
                result += 1
            if tmp2 == tmp2[::-1]:
                result += 1
    print(f"#{test_case} {result}")


