'''
Referencia al problema:
https://leetcode.com/problems/valid-anagram/
'''

def isAnagram(s, t):

    if len(s) != len(t):
        return False

    t_list = list(t)

    for char in s:
        if char in t_list: 
            t_list.remove(char) 
        else:
            return False 

    return True


'''
Example inputs:
anagram
nagaram
'''

s = input()
t = input()

print(isAnagram(s,t))