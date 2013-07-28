#!/usr/bin/env python3

import sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach())

from corpus import *
from math import log

mygermantokens = tokenize(loadTextFromFile ("germanText.txt"))
myfrenchtokens = tokenize(loadTextFromFile ("frenchText.txt"))

junksymbols = " ,;:-+=()[]'\"?!$%.<>´"

removeJunk(mygermantokens, junksymbols)
removeJunk(myfrenchtokens, junksymbols)

mygermandict = getTokenCounts(mygermantokens)
relativizeTokenCounts(mygermandict)

myfrenchdict = getTokenCounts(myfrenchtokens)
relativizeTokenCounts(myfrenchdict)

unknowntext = ""

ukntokens = tokenize(unknowntext)
hpgprob = 0.0
bbcprob = 0.0
for token in ukntokens:
    frenchprob += log(myfrenchdict.get(token, 0.000000000001))
    germanprob += log(mygermandict.get(token, 0.000000000001))
if frenchprob > germanprob:
    print("This text is probably French.")
else:
    print("This text is probably German")
print("frenchprob:", frenchprob)
print("germanprob:", germanprob)
