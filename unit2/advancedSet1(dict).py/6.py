'''
group_sizes is a list
in group_sizes, group_sizes[i] is the size of the group that pirate i should be in

we need to return a list of groups
the indexes are the ids in this case

plan:
- we use a dictionary size_to_pirates to bucket pirates by their required group size
- for each group size, we keep appending pirates to a temp list
- once the temp list hits the required group size we append it to the results list
- we reset temp list and continue until all of the pirates have been assigned

so we basically need to store it in the 

size: [pirate ids]
'''

from collections import defaultdict

def organize_pirate_crew(group_sizes):

    size_to_pirates = defaultdict(list)
    res = []

    #group pirates by the required group size
    for i, size in enumerate(group_sizes):
        size_to_pirates[size].append(i)
    
    #break each list into actual groups
    for size, pirates in size_to_pirates.items():
        temp = []
        for pirate in pirates:
            temp.append(pirate)
            if len(temp) == size:
                res.append(temp)
                temp = []
    
    return res



group_sizes1 = [3, 3, 3, 3, 3, 1, 3]
group_sizes2 = [2, 1, 3, 3, 3, 2]

print(organize_pirate_crew(group_sizes1))
print(organize_pirate_crew(group_sizes2)) 


            

            



























              


















































