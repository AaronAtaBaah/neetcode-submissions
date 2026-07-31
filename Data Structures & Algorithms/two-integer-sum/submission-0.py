class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0 
        j = 0
        hashfinder = 0 
        hashmap =  {}

        for number in range(len(nums)):
            hashfinder = target - nums[number]
            if (hashfinder in hashmap ):
                i = hashmap[hashfinder]
                j = number
                return[i,j]
            else : hashmap[nums[number]]= number
