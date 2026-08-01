class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # varible to store the current amount of 1s 
        currentones = 0 
        #varible to store the highest amount of ones
        maxones = 0
         #loop thorought the whole lsit as we are assesing the whole list 
        for number in nums:
        # cheeck if it's a one 
            if number == 1 :
             currentones +=1 # update when one is found
            if number != 1 :
                            currentones = 0
            if currentones > maxones:
                        maxones = currentones
            
        return maxones
                
                
                


     