import pandas as pd
import numpy as np
from csv import reader
from utils import *
from collections import defaultdict
import time
from itertools import permutations
from optparse import OptionParser


def aprioriFromFile(fname, minSup, minConf, minLift):
    C1ItemSet, itemSetList = getFromFile(fname)
    globalFreqItemSet = dict()
    globalItemSetWithSup = defaultdict(int)

    L1ItemSet = getAboveMinSup(C1ItemSet, itemSetList, minSup, globalItemSetWithSup)
    currentLSet = L1ItemSet
    k = 2
    while(currentLSet):
        globalFreqItemSet[k-1] = currentLSet
        candidateSet = getUnion(currentLSet, k)
        candidateSet = pruning(candidateSet, currentLSet, k-1)
        currentLSet = getAboveMinSup(candidateSet, itemSetList, minSup, globalItemSetWithSup)
        k += 1
    a= len(itemSetList)
    rules = associationRule(globalFreqItemSet, globalItemSetWithSup, minConf, minLift,a)

    return globalFreqItemSet, rules