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

def twoSum(self, nums: List[int], target: int) -> List[int]:
        used_nums = {}

        for i, val in enumerate(nums):
            look_for = target - val
            if look_for in used_nums.keys():
                return [i, used_nums[look_for]]
            else:
                used_nums[val] = i
        return -1