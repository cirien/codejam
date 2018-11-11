#!/usr/bin/python

import sys

def roundPercentage(decimal):
  if(decimal%1 >=0.5):
      return int(decimal) + 1
  return int(decimal)

f = open(sys.argv[1],'r')
t = int(f.readline())
# t = int(input()) 

for case in range(t):
  m = int(f.readline())
  countLanguages = [int(x) for x in f.readline().split()]
  percentage = 0
  responses = 0
  for language in range(l):
    percentage += roundPercentage(100*countLanguages[language]/n)
    responses += countLanguages[language]
  remaining = n-responses
  if remaining > 0:
    newLanguage = roundPercentage(100/n)
    newLanguage2 = roundPercentage(200/n)
    if(newLanguage2 >2*newLanguage):
      percentage += (newLanguage2-newLanguage)*remaining
    else:
      percentage += newLanguage*remaining
  print ("Case #" + str(case+1) + ": " + str(percentage))