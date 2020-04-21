# For the below DFS function to work the graph has to be in 
# list representation

def DFS(graph,node,visited):
    if(visited[node]):
        return
    visited[node] = True
    print(node)
    for adjNode in graph[node]:
        DFS(graph,adjNode,visited)

if __name__ == "__main__":
    graph = [
        [2,3],
        [3],
        [0,1],
        [0,1,2],
        [3,2,1]
    ]
    visited = [ False for i in range(len(graph)) ]
    DFS(graph,0,visited)