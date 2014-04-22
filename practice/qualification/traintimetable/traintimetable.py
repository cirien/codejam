#!/usr/bin/python

import sys

f = open(sys.argv[1],'r')
n = int(f.readline())

def convert_time(string):
  hh_mm = string.split(':')
  return (int(hh_mm[0])*60)+int(hh_mm[1])

for count in xrange(n):
  t = int(f.readline())
  na_nb = f.readline().split()
  na = int(na_nb[0])
  nb = int(na_nb[1])
  sa = na
  sb = nb
  a_times = []
  b_times = []
  for a in xrange(na):
    a_times.append(f.readline().split())
    a_times[a][0] = convert_time(a_times[a][0])
    a_times[a][1] = convert_time(a_times[a][1])
    a_times[a].append(False)
  for b in xrange(nb):
    b_times.append(f.readline().split())
    b_times[b][0] = convert_time(b_times[b][0])
    b_times[b][1] = convert_time(b_times[b][1])
    b_times[b].append(False)
  a_times = sorted(a_times, key=lambda a_time:a_time[0])
  b_times = sorted(b_times, key=lambda b_time:b_time[0])
  for a in xrange(na):
    for b in xrange(nb):
      if (a_times[a][1]+t)<= (b_times[b][0]) and (b_times[b][2] == False):
        b_times[b][2] = True
        sb = sb-1
        break
  for b in xrange(nb):
    for a in xrange(na):
      if (b_times[b][1]+t)<= (a_times[a][0]) and (a_times[a][2] == False):
        a_times[a][2] = True
        sa = sa-1
        break 
  print "Case #" + str(count+1) + ":",sa,sb
