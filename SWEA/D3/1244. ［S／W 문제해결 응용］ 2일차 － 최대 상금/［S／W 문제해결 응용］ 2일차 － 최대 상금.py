
T = int(input())

def find(cnt):
    global answer
    if cnt == count:
        answer= max(answer, int("".join(map(str, value))))
        return

    for i in range(length-1):
        for j in range(i+1,length):
            if not (i == 0 and value[j] == '0'):
                value[i],value[j] = value[j],value[i]
                chk = int("".join(map(str, value)))
                if (chk, cnt) not in visited:
                    visited.append((chk,cnt))
                    find(cnt+1)
                # 원상복구
                value[i], value[j] = value[j], value[i]

for tc in range(1, T + 1):
    number, count = map(int,input().split())
    value = list(str(number))
    length = len(value)
    visited = []
    answer = 0
    find(0)


    print(f"#{tc} {answer}")
