#!/usr/bin/env python
def SumTwo_noAuxSpace(numArr, TargetSum):
    """
    Pseudocode: 
        If numArr is already sorted O of n(log n),
        i = index
        i=0 -- min number
        j -- search begin from right n-1

        while i < j
            if numArr[j] == TargetSum - numArr[i]
                return True
            elif numArr[j] > TargetSum - numArr[j]
                j- = 1
            else
                i+=1
        
        return False
    """

def twoSum(self, nums: List[int], target: int) -> List[int]:
      used_nums = []
      for i, num1 in enumerate(nums):
          for j, num2 in enumerate(nums[:i])
              if num1+num2 = target
              return [i,j]
      return -1