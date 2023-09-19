INF=1000000000
def floyd_warshall(graph): # Function to find the shortest path using Warshall's algorithm
 num_vertices = len(graph)

 dist = [row[:] for row in graph] # Create a copy of the graph to store the shortest distances

 # Consider each vertex as an intermediate vertex and update the distances
 for k in range(num_vertices):
   for i in range(num_vertices):
       for j in range(num_vertices):
           dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

 return dist
 # Example graph represented as an adjacency matrix
graph = [ # Replace the values with float('inf') for unconnected vertices
[ 0, 5, INF, 10],
[ INF, 0, 3, INF],
[ INF, INF, 0, 1],
[INF, INF, INF, 0]
]
shortest_distances = floyd_warshall(graph)
 # Print the shortest distances between all pairs of vertices
for i in range(len(shortest_distances)):
   for j in range(len(shortest_distances[i])):
        print(f"Shortest distance from vertex {i} to vertex {j}: {shortest_distances[i][j]}")
