# def isValid(s: str) -> bool:
    
#     if ((len(s)) % 2) != 0:
#         return False
    
#     stack = []
#     mapping = {")": "(", "}": "{", "]": "["}
#     for char in s:
#         stack.append(char)
    
#     while stack != []:
#         if char in mapping:
#             if stack.pop(0) != mapping[stack.pop()]:
#                 return False

    
#     return True
# === INNCORRECT^ ===

class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        for c in s:
            if c in mapping:
                if stack and stack[-1] == mapping[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        if not stack:
            return True
        else:
            return False


if __name__ == "__main__":
    test_str = "((()))"
    assert isValid(test_str) == True

    test_str = "(()"
    assert isValid(test_str) == False

    test_str = "[(])"