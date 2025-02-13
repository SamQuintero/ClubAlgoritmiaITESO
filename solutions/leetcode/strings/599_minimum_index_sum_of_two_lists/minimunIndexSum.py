'''
Referencia al problema:
https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/
'''
def findRestaurant(list1, list2):
        
        min_sum = float('inf')
        result = []

        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:  
                    index_sum = i + j
                    if index_sum < min_sum:  
                        min_sum = index_sum
                        result = [list1[i]]
                    elif index_sum == min_sum:  
                        result.append(list1[i])
            
        return result

'''
Example inputs:
["Shogun","Tapioca Express","Burger King","KFC"]
["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
'''

list1 = [item.strip().strip('"').strip("'") for item in input().strip('[]').split(',')]
list2 = [item.strip().strip('"').strip("'") for item in input().strip('[]').split(',')]

print(findRestaurant(list1,list2))