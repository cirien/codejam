#!/usr/bin/python

import sys

t = int(input()) 

for case in range(t):
  n = int(input())
  values = [int(i) for i in input().split()]
  odd = sorted(values[::2])
  even = sorted(values[1::2])
  result = [0]*n
  result[::2] = odd
  result[1::2] = even
  sortstatus = "OK"
  for i in range(n-1):
    if result[i] > result[i+1]:
      sortstatus = str(i)
      break
  print ("Case #" + str(case+1) + ": " + sortstatus)