'''
- gold amounts is a list of integers of gold at each location
- we are given target which represents the amount of gold that is left

tp:
- make a dictionary with the format index : value
- for each index we need to see if there is a matching one that makes target 0 essentially
'''


def find_treasure_indices(gold_amounts, target):

    dictionary = {}
    
    for i in range(len(gold_amounts)):
        dictionary[i] = gold_amounts[i]
    
    for i in range(len(gold_amounts)):
        needed_value = target - gold_amounts[i]

        for j, value in dictionary.items():
            if value == needed_value and i != j:
                return [i, j]
    
    return []



gold_amounts1 = [2, 7, 11, 15]
target1 = 9

gold_amounts2 = [3, 2, 4]
target2 = 6

gold_amounts3 = [3, 3]
target3 = 6

print(find_treasure_indices(gold_amounts1, target1))  
print(find_treasure_indices(gold_amounts2, target2))  
print(find_treasure_indices(gold_amounts3, target3)) 