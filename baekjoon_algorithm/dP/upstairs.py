stair_count = int(input())
stair_scores_list = list()
stair_scores_list.append(0)

for i in range(stair_count):
    stair_scores_list.append(int(input()))

sum_of_score = list()
sum_of_score.append(0)
sum_of_score.append(stair_scores_list[1])
sum_of_score.append(stair_scores_list[1] + stair_scores_list[2])
sum_of_score.append(max(stair_scores_list[3] + stair_scores_list[1], stair_scores_list[3] + stair_scores_list[2]))

for i in range(4, stair_count + 1):
    sum_of_score.append(max(stair_scores_list[i] + sum_of_score[i - 2],stair_scores_list[i] + stair_scores_list[i - 1] + sum_of_score[i - 3]))

print(sum_of_score[-1])