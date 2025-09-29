# first solution, pretty dank, checks to see if the ascii value is the same
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []

        for word in strs:
            temp = []

            for word1 in strs:
                if sum(ord(char) for char in word) == sum(ord(char) for char in word1):
                    temp.append(word1)
            result.append(temp)

        return result
    

# second solution, uses a hashmap
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        bank = {}
        
        for word in strs:
            sortedWord = "".join(sorted(word))

            if sortedWord not in bank:
                bank[sortedWord] = [word]
            else:
                bank[sortedWord].append(word)

        return list(bank.values())
        
