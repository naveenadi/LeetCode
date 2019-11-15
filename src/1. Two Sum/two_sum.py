class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # if len(nums) < 2:
        #     pass
        hash_list = []
        for i in range(n := len(nums)):
            complement = target - nums[i]
            if complement in hash_list:
                return [i, nums.index(complement)]
            hash_list.append(nums[i])