#!/usr/bin/env python3
import sys
with open(sys.argv[1], 'r') as f:
    for line in f:
        list = line.split()
    	start_exons = list[9].split(",")
    	end_exons =list[10].split(",")

    	final_list = []
    	for item in xrange(0,len(start_exons)-1):
        	tmp_list = []
        	tmp_list.append(list[2][3:]+"\t")
        	tmp_list.append(start_exons[item]+"\t")
        	tmp_list.append(end_exons[item]+"\t")
        	final_list.append(tmp_list)
    	for row in final_list:
        	for col in row:
            		print col,
        	print 
