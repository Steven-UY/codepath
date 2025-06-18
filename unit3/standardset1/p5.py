'''
- put them into different arrays
- then we can have a pointer for each and increment them as it goes
- put it each into a result array
'''

def merge_schedules(schedule1, schedule2):

    pointer_1 = 0
    pointer_2 = 0

    res = ""

    while pointer_1 < len(schedule1) and pointer_2 < len(schedule2):

        res += schedule1[pointer_1]
        pointer_1 += 1

        res += schedule2[pointer_2]
        pointer_2 += 1
    
    if pointer_1 < len(schedule1):
        res += schedule1[pointer_1:]
    elif pointer_2 < len(schedule2):
        res += schedule2[pointer_2:]
    
    return res




print(merge_schedules("abc", "pqr")) 
print(merge_schedules("ab", "pqrs")) 
print(merge_schedules("abcd", "pq")) 