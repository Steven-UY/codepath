'''
we don't really need a stack here but whatever I guess lol

to use a stack we need...

'''

def collect_festival_points(points):
    
    total = 0 

    for i in range(len(points)):

        total += points[i]

    return total


print(collect_festival_points([5, 8, 3, 10])) 
print(collect_festival_points([2, 7, 4, 6])) 
print(collect_festival_points([1, 5, 9, 2, 8])) 
