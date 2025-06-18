'''
clue -> booth number 
back -> must backtrack to a previous booth

tp:
- use a queue here
- enqueue but when we encounter a "back" we pop
- return the queue at the end
'''

from collections import deque

def booth_navigation(clues):

    queue = deque([])

    for i in range(len(clues)):

        if clues[i] == "back" and queue:
            queue.pop()
        elif clues[i] != "back":
            queue.append(clues[i])

    return queue




clues = [1, 2, "back", 3, 4]
print(booth_navigation(clues)) 

clues = [5, 3, 2, "back", "back", 7]
print(booth_navigation(clues)) 

clues = [1, "back", 2, "back", "back", 3]
print(booth_navigation(clues)) 


'''
[1, 3, 4] -> we don't actually visit two here since we must backtrack
[5, 7]
[3]
'''