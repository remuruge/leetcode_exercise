class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            another = target - nums[i]
            if another in nums:
                try:
                    j = nums.index(another)
                    if i != j:
                        return [i, j]
                except ValueError as e:
                    # There has no item in list
                    continue
        return []