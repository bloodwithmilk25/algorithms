# initialization
# the graph
graph = {}
graph["start"] = {}
graph["start"]["a"] = 5
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["c"] = 4
graph["a"]["d"] = 2

graph["b"] = {}
graph["b"]["a"] = 8
graph["b"]["d"] = 7

graph["c"] = {}
graph["c"]["d"] = 6
graph["c"]["fin"] = 3

graph["d"] = {}
graph["d"]["fin"] = 1

graph["fin"] = {}

# the costs table
infinity = float("inf")
costs = {}
costs["a"] = 5
costs["b"] = 2
costs["c"] = infinity
costs["d"] = infinity
costs["fin"] = infinity

# the parents table
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["c"] = None
parents["d"] = None
parents["fin"] = None

graph = {}
graph["start"] = {}
graph["start"]["a"] = 10

graph["a"] = {}
graph["a"]["c"] = 1
graph["a"]["b"] = 20

graph["b"] = {}
graph["b"]["c"] = 1
graph["b"]["fin"] = 30

graph["c"] = {}
graph["c"]["a"] = 1

graph["fin"] = {}

# the costs table
infinity = float("inf")
costs = {}
costs["a"] = 10
costs["b"] = infinity
costs["c"] = infinity
costs["fin"] = infinity

# the parents table
parents = {}
parents["a"] = "start"
parents["b"] = None
parents["c"] = None
parents["fin"] = None

checked = []


# graph = {}
# graph['start'] = {}
# graph['start']['b'] = 4
# graph['start']['c'] = 2
#
# graph['b'] = {}
# graph['b']['c'] = 5
# graph['b']['d'] = 10
#
# graph['c'] = {}
# graph['c']['e'] = 3
#
# graph['d'] = {}
# graph['d']['fin'] = 11
#
# graph['e'] = {}
# graph['e']['d'] = 4
#
# graph['fin'] = {}
#
#
# infinity = float('inf')
# costs = {}
# costs['b'] = 4
# costs['c'] = 2
# costs['d'] = infinity
# costs['e'] = infinity
# costs['fin'] = infinity
#
# parents = {}
# parents['b'] = 'start'
# parents['c'] = 'start'
# parents['d'] = None
# parents['e'] = None
# parents['fin'] = None
#
# checked = []

def find_lowest_cots_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        if costs[node] < lowest_cost and node not in checked:
            lowest_cost = costs[node]
            lowest_cost_node = node
    return lowest_cost_node

def dejkstra_alg(graph):
    node = find_lowest_cots_node(costs)
    while node:
        neighbours = graph[node]
        for n in neighbours:
            new_cost = neighbours[n] + costs[node]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        checked.append(node)
        node = find_lowest_cots_node(costs)
    return costs

print(dejkstra_alg(graph))
