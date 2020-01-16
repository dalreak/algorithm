result = [0,1,1,1,2,2]
for j in range(int(input())):
    num = int(input())
    if len(result)-1 >= num:
        print(result[num])
    else:
        for i in range(len(result),num+1):
            result.append(result[i-1] + result[i-5])
        print(result[-1])