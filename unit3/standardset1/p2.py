'''
we need to use a queue to process requests in the order that they arrive but also ensure that the
requests with higher priorities are processed before those with the lower priorities.

the higher the number is within the tuple the higher the priority is:

tp:
we can use a priority queue to rank the values accordingly
'''

import heapq

def process_performance_requests(requests):

    priority_queue = []

    for index, (priority, name) in enumerate(requests):
        heapq.heappush(priority_queue, (-priority, index, name))
    
    processed_order = []

    while priority_queue:

        neg_priority, arrival_index, name = heapq.heappop(priority_queue)
        processed_order.append(name)
    
    return processed_order



print(process_performance_requests([(3, 'Dance'), (5, 'Music'), (1, 'Drama')]))
print(process_performance_requests([(2, 'Poetry'), (1, 'Magic Show'), (4, 'Concert'), (3, 'Stand-up Comedy')]))
print(process_performance_requests([(1, 'Art Exhibition'), (3, 'Film Screening'), (2, 'Workshop'), (5, 'Keynote Speech'), (4, 'Panel Discussion')]))



