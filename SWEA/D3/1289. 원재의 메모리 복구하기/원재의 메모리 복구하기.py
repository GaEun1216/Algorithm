
T = int(input())
for tc in range(1, T + 1):
    N = list(map(int,list(input())))
    result = 0
    for i in range(len(N)):
        if 1 not in N:
            break
        if N[i] == 1:
            for j in range(i,len(N)):
                N[j] = 1-N[j]
            result += 1


    print(f"#{tc} {result}")
