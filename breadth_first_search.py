from collections import deque

"""
1. Create queue with nodes that need to be cheched
2. Take next node out of the queue
3. Check if it's the node we're looking for.
4.A. YES - Done
4.B. NO - Mark node as checked. Add it's adjancent nodes to the queue.
5. Go to step 2
6. If queue is empty, search failed.
"""


graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

# any search function
def person_is_seller(name):
      return name[-1] == 'm'

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    # This array is how you keep track of which people you've searched before.
    searched = []
    while search_queue:
        person = search_queue.popleft()
        # Only search this person if you haven't already searched them.
        if person not in searched:
            # check if it's the right node
            if person_is_seller(person):
                print(person + " is a mango seller!")
                return True
            # if not, check it's adjacent nodes
            else:
                search_queue += graph[person]
                # Marks this person as searched
                searched.append(person)
    return False

search("you")
