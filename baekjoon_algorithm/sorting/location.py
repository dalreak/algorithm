import sys
result = list()
resultDict = dict()    
for i in range(int(sys.stdin.readline())):
    temp = sys.stdin.readline().split()
    resultDict[i] = temp[1]
    result.append((int(temp[0]),i))
for i in sorted(result):
    print(i[0],resultDict[i[1]])