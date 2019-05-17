def node_we_look_for(node):
    return node[-1] == "y"


def dfs(graph, node):
    return dfs_helper(graph, node, [])

def dfs_helper(graph, node, checked):
    if not node:
        return
    if node_we_look_for(node):
        return node

    checked.append(node)
    for n in graph[node]:
        if n not in checked:
            return dfs_helper(graph, n, checked)



graph = {}
graph["you"] = ["alice", "anatoly", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggan"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggan"] = ['thom']
graph["thom"] = ['biggy']
graph["jonny"] = []

# Although anatoly is closer, we should find biggy first. "you" -> "alice" -> "peggan" => "thom" => "biggy"
print(dfs(graph, 'you'))
