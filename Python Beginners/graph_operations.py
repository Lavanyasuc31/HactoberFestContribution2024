# Importing necessary libraries
import heapq
import networkx as nx
import matplotlib.pyplot as plt



# Class representing a graph
class Graph:
    def __init__(self):
        self.vertices = {}

    # Method to add a vertex to the graph
    def add_vertex(self, vertex):
        self.vertices[vertex] = {}

    # Method to add an edge between two vertices
    def add_edge(self, start, end, weight):
        self.vertices[start][end] = weight

    # Method to get all the vertices in the graph
    def get_vertices(self):
        return list(self.vertices.keys())

    # Method to get the neighbors of a vertex
    def get_neighbors(self, vertex):
        return list(self.vertices[vertex].keys())

    # Method to get the weight of an edge
    def get_weight(self, start, end):
        return self.vertices[start][end]

    # Dijkstra's algorithm for finding the shortest path
    def dijkstra(self, start):
        # Initialize distances and visited dictionary
        distances = {vertex: float('inf') for vertex in self.vertices}
        distances[start] = 0
        visited = {}

        # Create a priority queue and add the start vertex
        priority_queue = [(0, start)]

        while priority_queue:
            # Get the vertex with the minimum distance
            current_distance, current_vertex = heapq.heappop(priority_queue)

            # Skip if the vertex has already been visited
            if current_vertex in visited:
                continue

            # Mark the vertex as visited
            visited[current_vertex] = True

            # Update the distances of the neighboring vertices
            for neighbor in self.get_neighbors(current_vertex):
                distance = current_distance + self.get_weight(current_vertex, neighbor)
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances

    # Depth-first search (DFS) algorithm
    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)

        for neighbor in self.get_neighbors(start):
            if neighbor not in visited:
                self.dfs(neighbor, visited)

        return visited

# Example usage
if __name__ == "__main__":
    # Create a graph object
    graph = Graph()

    # Add vertices to the graph
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")
    graph.add_vertex("D")
    graph.add_vertex("E")

    # Add edges to the graph
    graph.add_edge("A", "B", 5)
    graph.add_edge("A", "C", 3)
    graph.add_edge("B", "D", 2)
    graph.add_edge("C", "D", 1)
    graph.add_edge("D", "E", 4)

    # Perform Dijkstra's algorithm
    start_vertex = "A"
    shortest_distances = graph.dijkstra(start_vertex)
    print("Shortest distances from vertex", start_vertex)
    for vertex, distance in shortest_distances.items():
        print(vertex, ":", distance)

    # Perform DFS
    start_vertex = "A"
    visited_vertices = graph.dfs(start_vertex)
    print("Visited vertices using DFS starting from", start_vertex)
    print(visited_vertices)




# Create a graph object
graph = nx.Graph()

# Add vertices to the graph
graph.add_nodes_from(["A", "B", "C", "D", "E"])

# Add edges to the graph
graph.add_edges_from([("A", "B"), ("A", "C"), ("B", "D"), ("C", "D"), ("D", "E")])

# Draw the graph
pos = nx.spring_layout(graph)  # Position nodes using the spring layout algorithm
nx.draw_networkx(graph, pos=pos, with_labels=True, node_color='lightblue', edge_color='gray')

# Draw edge weights
edge_labels = nx.get_edge_attributes(graph, 'weight')
nx.draw_networkx_edge_labels(graph, pos=pos, edge_labels=edge_labels)

# Show the graph
plt.title("Graph Visualization")
plt.axis('off')
plt.show()

