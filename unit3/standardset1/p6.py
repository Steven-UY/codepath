'''
understanding:
-> two arrays schedule1 and schedule2
-> schedule1 is a subset of schedule2
-> for each event in schedule1 find its position in schedule2 and determine the next event in
schedule2 that has a higher popularity score
-> add the scores to a result array

tp:
- nested loop
- try to find the schedule1 event in schedule2
- and then we need to see if an event has a higher value than it afterwards
- if it does then we add it to results
- if it doesn't then we just add -1

maybe we use a dictionary here actually, I believe that we can
actually just store schedule2 in a dictionary in the format index : value
we check for existence and we loop through from the index in schedule2 to the end.
If it exists within the 
'''

def next_greater_event(schedule1, schedule2):

    next_greater = {} #stores mappings like event: next_greater_event
    stack = [] #monotonic decreasing stack each new element pushed is less than or equal to the one before

    for num in schedule2:
        #
        while stack and num > stack[-1]:
            prev = stack.pop()
            next_greater[prev] = num
        stack.append(num)
    
    return [next_greater.get(x, -1) for x in schedule1]

        
print(next_greater_event([4, 1, 2], [1, 3, 4, 2])) 
print(next_greater_event([2, 4], [1, 2, 3, 4]))
