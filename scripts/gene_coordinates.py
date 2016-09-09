#!/usr/bin/env python3

with open("NM_007294.txt") as f:
    for line in f:
        list = line.split()
    start_exons = list[9].split(",")
    end_exons =list[10].split(",")

final_list = []
tmp_list = []
tmp_list.append(list[2])
tmp_list.append(int(start_exons[0]) - 2000)
tmp_list.append(int(end_exons[22]) + 2000)
final_list.append(tmp_list)
for row in final_list:
        for col in row:
            print col,
        print
