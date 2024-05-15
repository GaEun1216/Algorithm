T = int(input())
for test_case in range(1, T + 1):
    t, length = input().split()

    number = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    data = input().split()

    counts = {key: data.count(key) for key in number }
    
    print(t)
    for i in number:
        print(f'{i} '*counts[i],end= ' ')
    print()
