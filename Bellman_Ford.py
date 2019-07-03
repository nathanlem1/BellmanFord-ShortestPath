# Bellman Ford's shortest path Algorithm:
#
# Basically, a graph can be represented using either Adjacency matrix or Adjacency list, plsease visit the following
# link for more tutorial: https://www.hackerearth.com/practice/algorithms/graphs/graph-representation/tutorial/
#
# Bellman Ford's algorithm is used to find the shortest paths from the source vertex to all other vertices in a weighted
# undirected/directed graph that can have negative edge weights. For the problem to be well-defined, there should
# be no cycles in the graph with a NEGATIVE TOTAL WEIGHT!
# It depends on the following concept: Shortest path contains at most V-1 edges (V is the total number of vertices), because the
# shortest path couldn't have a cycle.
#
# So why shortest path shouldn't have a cycle ?
# There is no need to pass a vertex again, because the shortest path to all other vertices could be found without the need
# for a second visit for any vertices.
#
# Algorithm Steps:
# The outer loop traverses from  0: V-1
# Loop over all edges, check if the next node distance > current node distance + edge weight,
# in this case update the next node distance to "current node distance + edge weight". In other words, the update
# operation on an edge from vertex i to vertex j is distance[j] = min(distance[j], distance[i] + weight(i, j)).
#
# This algorithm depends on the relaxation principle where the shortest distance for all vertices is gradually replaced
# by more accurate values until eventually reaching the optimum solution. In the beginning all vertices have a distance
# of "Infinity", but only the distance of the source vertex = 0, then update all the connected vertices with the new distances
# (source vertex distance + edge weights), then apply the same concept for the new vertices with new distances and so on.

"""
The Bellman-Ford algorithm Graph API:
    iter(graph) gives all nodes
    iter(graph[neighbr]) gives neighbours of neighbr
    graph[neighbr][node] gives weight of edge (neighbr, node)
    This algorithm has time complexity of O(V.E) where
    V & E are the total number of vertices (nodes) and edges in the graph, respectively.
"""

def Bellman_Ford(graph, source):
    # Step 1: Prepare the distance and predecessor for each node, and then initialize a graph
    distance, predecessor = dict(), dict()
    for node in graph:
        distance[node] = float('inf')  # The rest of nodes are assumed to be very far i.e. in the beginning all vertices have a distance of "Infinity"
        predecessor[node] = None    # To indicate no predecessor
    distance[source] = 0    # For the source we know how to reach because source is 0 distance from itself.

    # Step 2: Relax the edge set V-1 times to find all shortest paths (V - number of vertices)
    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbour in graph[node]:
                # If the distance between the node and the neighbour is lower than the current, store it
                if distance[node] + graph[node][neighbour] < distance[neighbour]:
                    distance[neighbour], predecessor[neighbour] = distance[node] + graph[node][neighbour], node   # Record this lower distance
                # distance[neighbour], predecessor[neighbour] = min(distance[neighbour], distance[node] + graph[node][neighbour], distance[neighbour]), node     # the same!

    # Step 3: Check for negative weight cycles i.e. detect cycles if any
    for node in graph:
        for neighbour in graph[node]:
            assert distance[neighbour] <= distance[node] + graph[node][neighbour], "Graph contains a negative-weight cycle."

    return distance, predecessor


if __name__ == '__main__':

    # Adjaceny list is used for graph representation (rather than adjacency matrix)
    graph = {
        'a': {'b': -1, 'c': 4},
        'b': {'c': 3, 'd': 2, 'e': 2},
        'c': {},
        'd': {'b': 1, 'c': 5},
        'e': {'d': -3}
    }

    distance, predecessor = Bellman_Ford(graph, source='a')

    print distance

    graph = {
        'a': {'c': 3},
        'b': {'a': 2},
        'c': {'b': 7, 'd': 1},
        'd': {'a': 6},
    }

    distance, predecessor = Bellman_Ford(graph, source='a')

    print distance


    graph = {
        'a': {'b': 2, 'c': 5, 'd': 10},
        'b': {'c': -3},
        'c': {},
        'd': {'c': 4}
    }

    distance, predecessor = Bellman_Ford(graph, source='a')

    graph = {
        'a': {'b': 4, 'c': 10, 'd': 6, 'e': 2},
        'b': {'c': 5, 'd': 3, 'e': -5},
        'c': {'d': -10},
        'd': {'b': 30},      #NB: There should be no cycles in the graph with a negative TOTAL weight! 'd': {'b': v} where v is lower +ve or -ve value doesn't work!
        'e': {'d': -8}
    }

    distance, predecessor = Bellman_Ford(graph, source='a')

    print distance
    
    # Undirected graph
    graph = {
        'a': {'b': 0.1, 'c': 4, 'd': 2, 'e': 1},
        'b': {'a': 0.1, 'c': 3, 'd': 2, 'e': 2},
        'c': {'b': 3, 'a': 4, 'd': 5, 'e': 3},
        'd': {'c': 5, 'b': 2, 'a': 2, 'e': 0.3},
        'e': {'a': 1, 'b': 2, 'c': 3, 'd': 0.3},
    }
    distance, predecessor = Bellman_Ford(graph, source='a')
    print distance


