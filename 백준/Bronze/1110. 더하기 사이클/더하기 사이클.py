# 26부터 시작한다. 2+6 = 8이다. 새로운 수는 68이다. 
#6+8 = 14이다. 새로운 수는 84이다. 8+4 = 12이다. 새로운 수는 42이다. 4+2 = 6

value = int(input())
cnt = 1
a_val = value
while 1:
    b_val = a_val//10 + a_val%10
    a_val = (a_val%10)*10 + b_val%10
    if a_val == value:
        break
    cnt+=1
print(cnt)