## 55. Jump Game
## https://leetcode.com/problems/jump-game/description/
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        len_nums = len(nums)
        i=0
        len_jmp = nums[0]
        while i < len_nums:
            if i+len_jmp >= len_nums-1:
                return True
            elif len_jmp > 0:
                if i+1 < len_nums:
                    len_jmp -= 1
                    if nums[i+1] > len_jmp:
                        len_jmp = nums[i+1]
                    i += 1
            elif i < len_nums-1 and len_jmp == 0:
                return False
        return False