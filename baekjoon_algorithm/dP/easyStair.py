result = list()
result.append({"1","2","3","4","5","6","7","8","9"})
for i in range(1,int(input())+1):
    result.append(set())
    for d in result[i-1]:
        if int(d[0])-1 >= 0 and int(d[0])-1 != 9:
            result[i].add(str(int(d[0])-1) + d)
        if int(d[-1])-1 != 9:
            result[i].add(d + str(int(d[-1])-1))
        if int(d[-1])+1 != 10:
            result[i].add(d + str(int(d[-1])+1))
        if int(d[0])+1 != 10:   
            result[i].add(str(int(d[0])+1) + d)
print(sorted(list(result[-2])))