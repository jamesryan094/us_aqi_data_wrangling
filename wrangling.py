for i in range(2000, 2018):
    aqi_datafile = open("in/annual_aqi_by_cbsa_" + str(i) + ".csv")
    outfile = open("out/aqi_clean" + str(i) + ".csv", 'w')
    for line in aqi_datafile:
        temp = line.strip().split(',')
        clean_line = ''
        prefix = ''
        state_section = temp[1].strip().split('-')
        temp2 = temp
        for state in state_section:
            temp2[1] = state
            for element in temp2:
                clean_line += prefix + element
                prefix = ','
            outfile.write(clean_line + '\n')
            clean_line = ""
            prefix = ''
    aqi_datafile.close()
    outfile.close()

    # temp = line.strip()
    # temp = line.split(',')
    # if '-' in line[1]:
    #     states = line[1].strip()
    #     states = line[1].split('-')
    #     for state in states:
    #         pass
    # else:
    #     outfile.write(line)


# if '-' in state_section:
#     states = state_section.split('-')
# for state in states:
#     for element in temp:
#         clean_line += prefix + state_section
#         prefix = ','