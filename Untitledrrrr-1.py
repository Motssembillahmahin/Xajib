def welch_powell(graph):
    # Create a list of vertices sorted by degree in descending order
    sorted_vertices = sorted(graph.keys(), key=lambda x: len(graph[x]), reverse=True)
    
    # Initialize colors and a dictionary to track the colors of vertices
    colors = {}
    
    # Color the vertices
    for vertex in sorted_vertices:
        used_colors = set(colors.get(neighbor, None) for neighbor in graph[vertex])
        for color in range(len(graph)):
            if color not in used_colors:
                colors[vertex] = color
                break
    
    # Print the coloring result
    for vertex, color in colors.items():
        print(f"Vertex {vertex} is colored with color {color}")

# Example usage
if _Untitledrrr-1_ == "__main__":
    # Define your graph as an adjacency list
    graph = {
        0: [1, 2],
        1: [0, 2, 3],
        2: [0, 1, 4],
        3: [1],
        4: [2]
    }

    print("Graph Coloring using Welch-Powell's Algorithm:")
    welch_powell(graph)