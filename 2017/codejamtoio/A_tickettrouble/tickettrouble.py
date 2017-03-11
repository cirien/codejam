#!/usr/bin/python

import sys

f = open(sys.argv[1],'r')
t = int(f.readline())

for case in range(t):
  [n,s] = [int(i) for i in f.readline().split()]
  seats = [[0 for x in range(s)] for y in range(s)] 
  rows = [0 for x in range(s)]
  max = 0
  for friend in range(n):
    [x,y] = [int(i) for i in f.readline().split()]
    x= x-1
    y = y-1
    while(seats[x][y]==0):
      seats[x][y] = 1
      rows[x] += 1
      if (rows[x] > max):
        max = rows[x]
      x,y = y,x

  print ("Case #" + str(case+1) + ": " + str(max))