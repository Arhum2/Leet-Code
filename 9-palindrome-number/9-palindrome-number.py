class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = x
        rev_num = 0
        
        
        if x < 0:
            return False
        
        while y != 0:
            remainder = y % 10
            rev_num = rev_num * 10 + remainder
            y //= 10

            print(str(y), str(rev_num))
            
        if x < 0:
            return False
        
        elif x == rev_num:
            return True
        
        else:
            return False