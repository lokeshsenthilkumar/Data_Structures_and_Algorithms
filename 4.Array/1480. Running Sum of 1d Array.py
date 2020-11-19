# Solution 1:Using loops

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1,len(nums)):
            nums[i]=nums[i]+nums[i-1]
        return nums

# Solution 1:Using accumulate

from itertools import accumulate
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return accumulate(nums)

