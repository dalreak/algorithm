tri = list(map(int,input().split()))
while tri[0] != 0:
    temp = [0,1,2]
    temp.pop(tri.index((max(tri))))
    if max(tri) ** 2 == tri[temp[0]] ** 2 + tri[temp[1]] ** 2:
        print("right")
    else:
        print("wrong")
    tri = list(map(int,input().split()))