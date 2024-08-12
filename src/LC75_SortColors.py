#!/usr/bin/env python
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        if nums == []:
            return []
        else:
            Zs=Ts=i=0

            len_nums = len(nums)
            while i < len_nums:
                track = i-Ts
                if nums[track] == 0:
                    nums[track], nums[Zs] = nums[Zs], nums[track]
                    Zs+=1

                elif nums[track] == 2:
                    Ts += 1
                    nums[track], nums[len_nums-Ts] = nums[len_nums-Ts], nums[track]
                print(nums)
                i+=1