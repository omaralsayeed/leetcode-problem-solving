class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        maximum = max(nums)
        minimum = min(nums)
        counts = []
        for i in range(len(nums)):
            count = 0            
            for j in range(len(nums)):
                if nums[j] < nums[i]:
                    count+=1
            counts.append(count)
        
        return counts
            




        