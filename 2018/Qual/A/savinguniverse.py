#!/usr/bin/python

import sys

def trySwap(d,p):
  swaps = 0
  while(calculateDamage(p)>d):
    index = p.rfind("CS")
    if(index == -1):
      return "IMPOSSIBLE"
    commands = list(p)
    commands[index:index+2] = ['S','C']
    p = ''.join(commands)
    swaps +=1
  return swaps


def calculateDamage(p):
  currentPower = 1
  totalDamage = 0
  for c in p:
    if c=='C':
      currentPower = currentPower*2
    elif c=='S':
      totalDamage += currentPower
  return totalDamage

t = int(input()) 

for case in range(t):
  [d, p] = input().split()
  swapResult = trySwap(int(d),p)
  print ("Case #" + str(case+1) + ": " + str(swapResult))