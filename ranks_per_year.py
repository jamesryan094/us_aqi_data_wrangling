spend_data = open("env_spending_ranks.csv")
ranks = [[] for _ in range(5)]
for i, line in enumerate(spend_data):
    if i == 0:
        continue
    else:
        temp = line.strip().split(',')
        for j, element in enumerate(temp):
            if j % 3 == 0:
                ranks[j//3].append(element)

# 0: 2011, 4: 2015
ranks.reverse()

for year in ranks:
    print(year)

states = []
state_rank_change = [0 for _ in range(50)]
for state in ranks[0]:
    states.append(state)
states.sort()

yearly_ranks = [[0 for _ in range(50)] for _ in range(5)]
print(states)
for i, year in enumerate(ranks):
    for j, state in enumerate(year):
        for s, entry in enumerate(states):
            if state == entry:
                yearly_ranks[i][s] = j

differences = [0 for _ in range(50)]

for year in yearly_ranks:
    print(year)

for i in range(50):
    for j in range(1, 5):
        diff = yearly_ranks[j-1][i] - yearly_ranks[j][i]
        differences[i] += diff

# print(differences)
for_output = []
for i in range(50):
    temp_str = states[i] + ": " + str(differences[i])
    for_output.append(temp_str)

for out in for_output:
    print(out)
spend_data.close()
