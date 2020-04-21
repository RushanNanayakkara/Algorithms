if __name__ == "__main__":
    
    

    ## First line contains the number of vertices in the graph(n)
    ## and the number of edges in the graph(e)
    ## Next e lines contains the pairs of nodes that is connected
    ## by an edge 

# Graph - List representation   
    n,e  = list(map(int,input().split()))
    graph = [[] for i in range(n)]
    for i in range(e):
        a,b = list(map(int,input().split()))
        graph[a].append(b)
        graph[b].append(a)

# Graph - Matrix representation
    n,e  = list(map(int,input().split()))
    matrixGraph = [ [0 for i in range(n)] for j in range(n)]
    for i in range(e):
        a,b = list(map(int,input().split()))
        matrixGraph[a][b] = 1
        matrixGraph[b][a] = 1

# Graph - Edge list representation
    n,e  = list(map(int,input().split()))
    edgeGraph = [ list(map(int,input().split())) for i in range(e)]
    # Following code will explain the process of the above line
    ## edgeGraph1 = []
    ## for i in range(e):
    ##     a,b = list(map(int,input().split()))
    ##     edgeGraph.append([a,b])


    ## First line contains the number of vertices in the graph(n)
    ## and the number of edges in the graph(e)
    ## Next e lines contains three numbers, the first two represents a pair of nodes that are connected
    ## by an edge and the third value represents the weight of the edge
 

# Weighted  Graph - List representation
    n,e  = list(map(int,input().split()))
    weightedGraph = [ [] for i in range(n) ] 
    for i in range(e):
        a,b,w = list(map(int,input().split()))
        weightedGraph[a].append([b,w])
        weightedGraph[b].append([a,w])

# Weighted Graph - Matrix representation
    n,e  = list(map(int,input().split()))
    weightedMatrixGraph = [[ 0 for i in range(n)] for j in range(n) ]
    for i in range(e):
        a,b,w = list(map(int,input().split()))
        weightedMatrixGraph[a][b] = w
        weightedMatrixGraph[b][a] = w

# Weighted Graph - Edge list representation
    n,e  = list(map(int,input().split()))
    weightedEdgeGraph = [ list(map(int,input().split())) for i in range(e)]
    # Following code will explain the process of the above line
    edgeGraph1 = []
    for i in range(e):
        a,b,weight = list(map(int,input().split()))
        weightedEdgeGraph.append([a,b,weight])
