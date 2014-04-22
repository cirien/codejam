#!/usr/bin/python

import sys

f = open(sys.argv[1],'r')
n = int(f.readline())
for count in xrange(n):
  c = int(f.readline())
  i = int(f.readline())
  p = f.readline().split()
  for j in xrange(i):
    for k in xrange(len(p)-j-1):
      if(int(p[j])+int(p[j+k+1])  == c):
        print "Case #" + str(count+1) + ": ", str(j+1), str(j+k+2)
        break
