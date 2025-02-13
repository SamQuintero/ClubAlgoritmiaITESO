#https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/

#global variables
letters_for_number = {}
combinations = []

def backtrack(digits, i, combination):
    global combinations

    if i == len(digits): #caso base
        combinations.append(combination)
        return
    else: #caso recursivo
        for letter in letters_for_number[digits[i]]:
            backtrack(digits, i + 1, combination + letter)

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []

        global letters_for_number
        global combinations
        letters_for_number['2'] = ('a', 'b', 'c')
        letters_for_number['3'] = ('d', 'e', 'f')
        letters_for_number['4'] = ('g', 'h', 'i')
        letters_for_number['5'] = ('j', 'k', 'l')
        letters_for_number['6'] = ('m', 'n', 'o')
        letters_for_number['7'] = ('p', 'q', 'r', 's')
        letters_for_number['8'] = ('t', 'u', 'v')
        letters_for_number['9'] = ('w', 'x', 'y', 'z')
        combinations = []
        backtrack(digits, 0, "")
        return combinations