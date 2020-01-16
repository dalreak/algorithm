result = [0,1]
for i in range(2,int(input())+2):
    result.append((result[i-1] + result[i-2])%15746)
print(result[-1])