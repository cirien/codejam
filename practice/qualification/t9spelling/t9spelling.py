#!/usr/bin/python

import sys

f = open(sys.argv[1],'r')
n = int(f.readline())

for count in xrange(n):
  words = f.readline().split()
  print "Case #" + str(count+1) + ": ",
  for i in xrange(len(words)):
    if(i == len(words)-1):
      print words[len(words)-i-1]
    else:
      print words[len(words)-i-1],
