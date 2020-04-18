graph= dict()

graph['A']=['B','C']
graph['B']=['A','D']
graph['C']=['A','G','H','I']
graph['D']=['B','E','F']
graph['E']=['D']
graph['F']=['D']
graph['G']=['C']
graph['H']=['C']
graph['I']=['C','J']
graph['J']=['I']



def dfs1(graph, start_node):
    visited, need_visit = list(), list()
    need_visit.append(start_node)

    while need_visit:
        node = need_visit.pop()
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])

    return visited

print(dfs1(graph,'A'))


def dfs2(graph,start_node,visited=[]):

    visited.append(start_node)

    for node in graph[start_node]:
        if node not in visited:
            dfs2(graph,node,visited)
    return visited

print(dfs2(graph,'A'))