num = int(input())
result = list()
result.append(set())
result[0].add((num,0))
check = True
temp = 0
while check:
    check = False
    result.append(set())
    for d in result[temp]:
        if d[0] != 1:
            if d[0] % 3 == 0:
                result[temp+1].add((d[0]//3,d[1] + 1))
            if d[0] % 2 == 0:
                result[temp+1].add((d[0]//2,d[1] + 1))
            result[temp+1].add((d[0]-1,d[1]+1))
            check = True
        else:
            #result[temp+1].add((d[0],d[1]))
            check = False
            break
    temp = temp + 1

print(min(result[-1] | result[-2])[1])
