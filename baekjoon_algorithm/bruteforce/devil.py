num = 664
result_list = list()
count = int(input())
while len(result_list) != count:
    num = num + 1
    if "666" in str(num):
        result_list.append(num)
print(result_list[-1])