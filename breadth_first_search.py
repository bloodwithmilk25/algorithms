from collections import deque

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
