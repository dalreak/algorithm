chess = list()
result = list()
oposite = [1,0]
height,width = map(int,input().split())
for i in range(height):
    temp = input()
    temp = temp.replace("W","1")
    temp = temp.replace("B","0")
    chess.append(list(map(int,list(temp))))
#print(chess)
for h in range(height - 7):
    for w in range(width - 7):
        count = 0
        countT = 1
        temp_chess = list()
        temp_chessT = list()
        for i in chess[h:h+8]:
            temp_chess.append(i[w:w+8])
            temp_chessT.append(i[w:w+8])
        temp_chessT[0][0] = oposite[temp_chessT[0][0]]
        for i in range(1,8):
            if temp_chess[i][0] == temp_chess[i-1][0]:
                temp_chess[i][0] = oposite[temp_chess[i][0]]
                count = count + 1
            if temp_chessT[i][0] == temp_chessT[i-1][0]:
                temp_chessT[i][0] = oposite[temp_chessT[i][0]]
                countT = countT + 1
        for i in range(8):
            for v in range(1,8):
                if temp_chess[i][v] == temp_chess[i][v-1]:
                    temp_chess[i][v] = oposite[temp_chess[i][v]]
                    count = count +1
                if temp_chessT[i][v] == temp_chessT[i][v-1]:
                    temp_chessT[i][v] = oposite[temp_chessT[i][v]]
                    countT = countT +1
        result.append(countT)
        result.append(count)
print(min(result))
