class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = len(nums)-1
        nums1 = sorted(nums)
        while i<j:
            tar = nums1[i]+nums1[j]
            if tar == target:
                # We wrap the output array in sorted() to guarantee ascending index order
                if nums.index(nums1[i]) != nums.index(nums1[j]):
                    return sorted([nums.index(nums1[i]), nums.index(nums1[j])])
                else:
                    return sorted([nums.index(nums1[i]), nums.index(nums1[j], nums.index(nums1[i])+1)])
            elif tar < target:
                i+=1
            else:
                j-=1
