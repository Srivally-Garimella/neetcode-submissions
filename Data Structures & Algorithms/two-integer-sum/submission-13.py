class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq = {}
        for i in range (len(nums)):
            find = target - nums[i]
            if find in freq:
                return [freq[find],i]
            else:
                freq[nums[i]] = i







       
       
       
       
       
       
       
       
       
       
       
       
       
        # nummap = {}
        
        # for i in range(len(nums)):
        #     find = target - nums[i]
        #     if find in nummap:
        #         return [nummap[find],i]
        #     else:
        #         nummap[nums[i]]=i