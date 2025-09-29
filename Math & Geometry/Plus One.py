
from typing import List


def plusOne(digits: List[int]) -> List[int]:        
    # Reverse the list to make it easier to add 1 to the last element
    digits = digits[::-1]
    carry, i = 1, 0

    while carry == 1:
        if i < len(digits):
            if digits[i] == 9:
                digits[i] = 0 
            else:
                digits[i] += 1
                carry = 0


        else:
            digits.append(carry)
            carry = 0
        
        i += 1

    digits = digits[::-1]
    
    return digits

plusOne([1,2,9]) # [1,2,4]
