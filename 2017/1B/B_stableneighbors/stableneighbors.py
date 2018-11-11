#!/usr/bin/python

import sys

f = open(sys.argv[1],'r')
t = int(f.readline())

for case in range(t):
	print ("Case #" + str(case+1) + ": ", end = "")
	[N, R, O, Y, G, B, V] = [int(i) for i in f.readline().split()]
	small = [[R, "R"], [Y, "Y"], [B,"B"]]
	small.sort(key =lambda color: color[0], reverse = True)
	if(small[0][0]>small[1][0]+small[2][0]):
		print("IMPOSSIBLE")
	else:
		i = 1
		first = small[0][1]
		last = small[0][1]
		print(small[0][1], end = "")
		small[0][0] -= 1
		while i < N:
			small.sort(key =lambda color: color[0], reverse = True)
			if(small[0][1] != last):
				print(small[0][1], end = "")
				small[0][0] -= 1
			else:
				print(small[1][1], end = "")
				small[1][0] -= 1
		print("")
