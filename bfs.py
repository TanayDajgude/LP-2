graph = {'5':['3','8'],'3':['7','9'],'7':[],'9':[],'8':['2','4'],'2':[],'4':[]}
visited = []
queue = []


def bfs(visited,graph,node):
    if node not in visited:
        visited.append(node)
        queue.append(node)


        while queue:
            m = queue.pop(0)
            print(m,end="")

            for neighbour in graph[m]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)


print("Breadth first search for the following is :")
bfs(visited,graph,'5')
