#!/usr/bin/python

import sys
import math

f = open(sys.argv[1],'r')
t = int(f.readline())
for case in range(t):
  [d,n] = [int(z) for z in f.readline().split()]
  print ("Case #" + str(case+1) + ": ")
  if(n==0):
   print("I")
   continue
  x,y=0,0
  i,j=0,0
  flip = False
  firstRow = True
  result=[]
  while(n > 0):
    # continue to next rowblock
    if(j>=d):
      if(firstRow):
        i+=1
      firstRow = False
      flip = not flip
      i+=2
      j=0
      continue
    #otherwise, add on to current rowblock
    if(j<2):
      n-=1
    elif(n>2):
      n-=3
    else:
      if(firstRow):
        i+=1
      else:
        n-=1
      firstRow = False
      if(j+1<=y and y>2):
        result[i] = result[i][:-1]
        result[i+1] = result[i+1][:-1]
        j-=1
      while(j+1<=y):
        j+=1
        if(j+1==y and y>2):
          flip = not flip
        if(flip):
          result[i]+="I"
          result[i+1]+="O"
        else:
          result[i]+="O"
          result[i+1]+="I"
      flip = not flip
      i+=2
      j=0
      n-=1
    #create new rows if necessary
    if(firstRow and x<i+3):
      x+=3
      result.append("")
      result.append("")
      result.append("")
    elif(x<i+2):
      x+=2
      result.append("")
      result.append("")
    #append the new rows
    if(firstRow):
      result[i]+="I"
      result[i+1]+="/"
      result[i+2]+="O"
    elif(flip):
      result[i]+="/"
      result[i+1]+="I"
    else:
      result[i]+="/"
      result[i+1]+="O"
    j+=1
    if(j>y):
      y+=1
  if(j+1<=y and y>2):
    result[i] = result[i][:-1]
    result[i+1] = result[i+1][:-1]
    j-=1
  while(j+1<=y):
    j+=1
    if(j+1==y and y>2):
      flip = not flip
    if(flip):
      result[i]+="I"
      result[i+1]+="O"
    else:
      result[i]+="O"
      result[i+1]+="I"
  for p in result:
    print(p)