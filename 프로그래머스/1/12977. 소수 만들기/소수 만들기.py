def prime():
    pri = [0,0]+[1]*2999
    for i in range(2,3001):
        if pri[i] == 1:
            for j in range(2*i,3001,i):
                pri[j]=0
    return pri

def solution(nums):
    answer = 0
    pri = prime()
    l = len(nums)
    for i in range(l-2):
        for j in range(i+1,l-1):
            for k in range(j+1,l):
                a,b,c = nums[i],nums[j],nums[k]
                if pri[a+b+c]== 1:
                    answer += 1
    return answer