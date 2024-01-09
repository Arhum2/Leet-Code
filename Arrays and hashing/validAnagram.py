# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         dict = {}
        
#         for letter in t:
#             dict[letter] = 0
        
#         for letter in s:
#             if letter not in dict:
#                 return False
            
#         return True

# NOTES: tried using a dict to make it faster but this dosent work in the even that t is longer then s


### SOLUTION 2 ###
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         slst = []
#         for letter in s:
#             slst.append(letter)

#         tlst = []
#         for letter in t:
#             tlst.append(letter)
        
#         if sorted(slst) == sorted(tlst):
#             return True
        
#         return False

# NOTES: works but meh Runtime 61 ms Beats 26.34% Memory 19.4 MB Beats 6.43%


### SOLUTION 3 ###
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if sorted(s) == sorted(t):
#             return True
#         return False

# NOTES: Faster and uses less memory (Runtime 55 ms Beats 50.79% Memory 18.2 MB)



### SOLUTION 4 ###
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:

#         if len(s) != len(t):
#             return False

            
#         elif sorted(s) == sorted(t):
#             return True
#         return False

# NOTES: Faster and uses less memory Runtime 51 ms Beats 67.80% Memory 18.4 MB Beats 6.43%

## SOLUTION 5 ###
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        counts = {}
        countt = {}

        for i in range(len(s)):
            counts[s[i]] = 1 + counts.get(s[i], 0) #.get returns the value of the dictionary at key s[i], if it does not exist it uses 0 as the value
            countt[t[i]] = 1 + counts.get(s[t], 0) 
        
        for c in counts:
            if counts[c] != countt.get(c, 0):
                return False
        
        return True
       

# NOTES: Neet Code sol Runtime 46 ms Beats 84.55% Memory 17.7 MB Beats 27.75%

if __name__ == "__main__":
    sol = Solution()

    print(sol.isAnagram("ab", "a")) # false
