class Solution:
    def isPalindrome(self, s: str) -> bool:
       
        clean_text = "".join(char for char in s if char.isalnum())
        x =clean_text.upper() 
        startindex = 0 
        endindex = len(x)-1
        while startindex <= endindex:
             
            if (x[startindex] != x[endindex]):

                return False
            else :
                startindex +=1
                endindex -=1


        return True
        