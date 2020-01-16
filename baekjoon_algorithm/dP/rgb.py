class point:
    def __init__(self,value):
        self.value = value
    def nextPoint(self,lValue,rValue):
        if lValue < rValue:
            self.value = lValue
        else:
            self.value = rValue
    def getValue(self):
        return self.value

num = int(input())
r,g,b = map(int,input().split())
cList = [point(r),point(g),point(b)]
for i in range(1,num):
    r,g,b = map(int,input().split())
    pR = cList[0].getValue()
    pG = cList[1].getValue()
    pB = cList[2].getValue()
    cList[0].nextPoint(pG + r,pB + r)
    cList[1].nextPoint(pR + g,pB + g)
    cList[2].nextPoint(pR + b,pG + b)
print(min(cList[0].getValue(),cList[1].getValue(),cList[2].getValue()))
    
