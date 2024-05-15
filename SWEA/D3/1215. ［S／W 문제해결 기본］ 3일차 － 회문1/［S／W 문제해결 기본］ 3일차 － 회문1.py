T = 10 #int(input())
for test_case in range(1, T + 1):
    length = int(input())
    string = [ list(input()) for _ in range(8)]
    string_2 = list(zip(*string))

    result = []
    for i in range(8):
        for j in range(8-length+1):
            tempstr = string[i][j:j+length]
            tempstr2 = string_2[i][j:j+length]

            if tempstr == tempstr[::-1]:
                result.append(tempstr)
            if tempstr2 == tempstr2[::-1]:
                result.append(tempstr2)



    print(f"#{test_case} {len(result)}")


