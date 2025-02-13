'''
Referencia al problema:

https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/
'''

def strStr(haystack, needle):

    if len(needle) > len(haystack):
        return -1

    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i] == needle[0]:
            flag = True
            for j in range(1, len(needle)):
                if haystack[i + j] != needle[j]:
                    flag = False
                    break
                
            if flag:
                return i

        return -1
    
'''
sadbutsad
sad
'''

haystack = input()
needle = input()

print(strStr(haystack,needle))