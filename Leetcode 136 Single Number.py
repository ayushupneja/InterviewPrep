class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        i = 0
        while(1 == 1):
            if i<len(nums)-1:
                if nums[i] == nums[i+1]:
                    i+=2
                else:
                    return nums[i]
            else:
                return nums[i]
