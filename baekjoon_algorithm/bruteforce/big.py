class person:
    def __init__(self,data):
        super().__init__()
        self.height = data[1]
        self.weight = data[0]
people_list = list()
for i in range(int(input())):
    people_list.append(person(list(map(int,input().split()))))
for i in range(len(people_list)):
    count = 1
    for data in people_list:
        if people_list[i].height < data.height and people_list[i].weight < data.weight:
            count = count + 1
    print(count,end=" ") 
    