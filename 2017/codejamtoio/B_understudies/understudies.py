#!/usr/bin/python

import sys

f = open(sys.argv[1],'r')
t = int(f.readline())

for case in range(t):
  n = int(f.readline())
  cast = [float(i) for i in f.readline().split()]
  cast.sort()
  prob = 1.0
  for role in range(n):
    prob *= (1-(cast[role] * cast[2*n-role-1]))
  print ("Case #" + str(case+1) + ": " + str(prob))