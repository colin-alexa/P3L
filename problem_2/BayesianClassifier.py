#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


import sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach())

from dcavarCorpus import *
from math import log

mygermantokens = [a for a in getTextFromFile ("germanText.txt")]
myfrenchtokens = [a for a in getTextFromFile ("frenchText.txt")]

# junksymbols = " ,;:-+=()[]'\"?!$%.<>`"
# 
# removeJunk(mygermantokens, junksymbols)
# removeJunk(myfrenchtokens, junksymbols)

mygermandict = getNGramModel(mygermantokens, 3)
relativizeFP(mygermandict)

myfrenchdict = getNGramModel(myfrenchtokens, 3)
relativizeFP(myfrenchdict)

# testText = getTextFromFile("GermanCompanies.txt")

companies = getTextFromFile("FrenchCompanies.txt").splitlines()
companies = [ (a,getNGramModel(a,3)) for a in companies]

# ukntokens = getNGramModel(testText,3)

for company in companies:
  frenchprob = 0.0
  germanprob = 0.0
  for token in company[1]:
      frenchprob += log(myfrenchdict.get(token, 0.000000000001))
      germanprob += log(mygermandict.get(token, 0.000000000001))
  if frenchprob > germanprob:
      print( company[0] + "; This text is probably French.")
  elif germanprob > frenchprob:
      print( company[0] + "; This text is probably German.")
  else:
      print( company[0] + "; The classifier could not distinguish the languages.")
  print("frenchprob:", frenchprob)
  print("germanprob:", germanprob, '\n')
