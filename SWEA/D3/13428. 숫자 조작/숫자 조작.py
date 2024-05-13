from collections import deque

T = int(input())

def swap(i,j,string):
    list_copy = list(string).copy()
    list_copy[i],list_copy[j] = list_copy[j],list_copy[i]
    return ''.join(list_copy)

for tc in range(1, T + 1):
    number = input()
    min_r = int(number)
    max_r = int(number)
    length = len(number)
    for i in range(length-1):
        for j in range(i+1,length):
            temp = swap(i,j,number)
            number2 = int(temp)
            if temp[0] == '0': continue
            min_r = min(min_r,number2)
            max_r = max(max_r,number2)
    print(f"#{tc} {min_r} {max_r}")
