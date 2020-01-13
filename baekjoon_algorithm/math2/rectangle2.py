result_x,result_y = list(),list()
for i in range(3):
    x,y = map(int,input().split())
    if x not in result_x:
        result_x.append(x)
    else:
        result_x.remove(x)
    
    if y not in result_y:
        result_y.append(y)
    else:
        result_y.remove(y)
    
print(result_x[0],result_y[0])