#!/usr/bin/env python3

with open("NM_007294.txt") as f:
    for line in f:
        list = line.split()
    start_exons = list[9].split(",")
    end_exons =list[10].split(",")

    final_list = []
    for item in range(0,23):
        tmp_list = []
        tmp_list.append(list[2]+"\t")
        #tmp_list.append(list[3])
        tmp_list.append(start_exons[item]+"\t")
        tmp_list.append(end_exons[item])
        #tmp_list.append(list[1])
        #tmp_list.append(list[8])
        final_list.append(tmp_list)
    for row in final_list:
        for col in row:
            print col,
        print 
