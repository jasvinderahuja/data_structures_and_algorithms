#!/usr/bin/env python
def SumTwo_hashTable(numArr, SumTarget):
    """
    Pseudocode:
        Hashtable = []
        for i in range(len(numArr)):
            if len(Hashtable) == 0:
                Hashtable = numArr[i]
            else
                for j in range(len(Hashtable)):
                    if numArr[i] = SumTarget - Hash[j]:
                        return = True
            Hashtable.append(numArr[i]) ## use a Tupple tupple avoids duplicates
                        
    """