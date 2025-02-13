'''
Referencia al problema:
https://leetcode.com/problems/find-common-characters/description/
'''

def commonChars(words):

    common = list(words[0])  

    for i in range(1, len(words)):
        current_string = words[i]
        new_common = []

        for char in common:
            if char in current_string:
                new_common.append(char)
                current_string = current_string.replace(char, '', 1)

        common = new_common 

    return common


'''
Example input:
["bella","label","roller"]
'''
words = [item.strip().strip('"').strip("'") for item in input().strip('[]').split(',')]

print(commonChars(words))