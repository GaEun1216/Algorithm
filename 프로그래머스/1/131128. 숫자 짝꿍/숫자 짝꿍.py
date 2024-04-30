def solution(X, Y):
    ans = ""
    '''
    딕셔너리 사용
    예외 상황 : 0만 여러개 일때, 해당되는게 없을 때
    '''
    x = {str(n):0 for n in range(10)}
    y = {str(n):0 for n in range(10)}
    for i in X:
        x[i]+= 1
    for i in Y:
        y[i]+= 1
    for i in range(9,-1,-1):
        i = str(i)
        cnt = min(x[i],y[i])
        
        if len(ans) == 0 and i == '0' and cnt != 0:
            return "0"
        ans = ''.join([ans,i*cnt])
    if len(ans) == 0:
        return "-1"
    return ans
            
        