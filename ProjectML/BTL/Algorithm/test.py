from apriori import *
from utils import *

def check(rules, itemSetList):
    count=0
    for rule in rules:
        for itemSet in itemSetList:
            if rule.issubset(itemSet):
                count=count+1
                break

    return count
    
if __name__ == "__main__":
    fname="BTL/Data/groceries.csv"
    freqItemSet, rules = aprioriFromFile(fname, 0.03, 0.3,1)
    # print(rules)
    mylist=[]
    for i, k, m,n in rules:
        print("Rule: ",i, "=>",k )
        print("Conf: ",m)
        print("Lift: ",n)
        k= i.union(k)
        mylist.append(k)
    # print(mylist)
    fname1="BTL/Data/test1.csv"
    m, n= getFromFile(fname1)

    a= check(mylist,n)
    print("Accuracy:",a/len(rules)*100)
