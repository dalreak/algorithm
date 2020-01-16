class point:
    def __init__(self,cost):
        self.cost = int(cost)
        self.value = 0
    def insertValue(self,value):
        if self.value < value:
            self.value = value
    def getCost(self):
        return self.cost
    def getValue(self):
        return self.value
pList = list()
cList = list()
num = int(input()) + 1
cList.append(point(int(input())))
cList[0].insertValue(cList[0].getCost())
for i in range(2,num):
    pList = cList
    cList = list(map(lambda x: point(x),input().split()))
    for j,v in enumerate(pList):
        cList[j].insertValue(v.getValue() + cList[j].getCost())
        cList[j+1].insertValue(v.getValue() + cList[j+1].getCost())
print(max([x.getValue() for x in cList]))

