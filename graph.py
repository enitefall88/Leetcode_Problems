from collections import deque
graph = {}
graph['you'] = ['alice', 'bob', 'claire']
graph['alice'] = ['zed', 'marlem']
graph['marlem'] = ['zik', 'zak']
search_queue = deque()
search_queue += graph['you']

def person_is_seller(name):
    return name[-1] == 'm'

def bfe(graph, search_queue,):
    while search_queue: # while the queue is not empty
        #grab the first person of the queue
        person = search_queue.popleft()
        if person_is_seller(person):
            print(f"{person} is a mango seller!")
            return True
        else:
            search_queue += graph[person]
            print("nay")
            return False

bfe(graph=graph, search_queue=search_queue)
