num = input()
#digit_sum = sum([int(i) for i in num])
max_sum = 0
result = 0
for i,v in enumerate(num):
    if i == 0:
        max_sum += int(v) -1
    else:
        max_sum += 9
for i in range(int(num) - max_sum,int(num)):
    if i + sum([int(v) for v in str(i)]) == int(num):
        result = i
        break
print(result)
