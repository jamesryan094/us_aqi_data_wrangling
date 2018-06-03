# # Todo: Regenerate without dist. Coloumbia, Puerto Rico
#
# for i in range(2000, 2018):
#     aqi_datafile = open("in/annual_aqi_by_cbsa_" + str(i) + ".csv")
#     outfile = open("aqi_clean_all_mainland_averaged.csv", 'a')
#     for line in aqi_datafile:
#         temp = line.strip().split(',')
#         clean_line = ''
#         prefix = ''
#         state_section = temp[1].strip().split('-')
#         temp2 = temp
#         if "PR" in state_section or "DC" in state_section:
#             continue
#         for state in state_section:
#             temp2[1] = state
#             for j, element in enumerate(temp2):
#                 if j in {1,13,3}:
#                     clean_line += prefix + element
#                     prefix = ','
#             if clean_line == "State,Year,Median AQI" and i != 2000:
#                 clean_line = ""
#                 prefix = ''
#             else:
#                 outfile.write(clean_line + '\n')
#                 clean_line = ""
#                 prefix = ''
#     aqi_datafile.close()
#     outfile.close()

my_data = open("aqi_clean_all_mainland.csv")
my_matrix = [[] for _ in range(18)]
for i, line in enumerate(my_data):
    if i != 0:
        temp = line.split(',')
        if temp[0] not in my_matrix[int(temp[1])-2000]:
            my_matrix[int(temp[1])-2000].append(temp[0])
my_data.close()

for year in my_matrix:
    print(len(year))
