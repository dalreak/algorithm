z_count = [1,0]
o_count = [0,1]
num = int(input())
if len(z_count) < num + 1:
    for i in range(len(z_count),num + 1):
        z_count.append(z_count[-1] + z_count[-2])
        o_count.append(o_count[-1] + o_count[-2])
    print(o_count[-1])
else:
    print(o_count[num])