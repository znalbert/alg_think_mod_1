"""
Algorithmic Thinking - Project 1
"""

EX_GRAPH0 = {0: set([1, 2]),
        1: set([]),
        2: set([])}
EX_GRAPH1 = {0: set([1, 4, 5]),
        1: set([2, 6]),
        2: set([3]),
        3: set([0]),
        4: set([1]),
        5: set([2]),
        6: set([])}
EX_GRAPH2 = {0: set([1, 4, 5]),
        1: set([2, 6]),
        2: set([3, 7]),
        3: set([7]),
        4: set([1]),
        5: set([2]),
        6: set([]),
        7: set([3]),
        8: set([1, 2]),
        9: set([0, 3, 4, 5, 6, 7,])}

def make_complete_graph(num_nodes):
    """ int -> dict
    Takes an integer and returns a dictionary of a complete digraph containing
    that many nodes.
    """
    graph = {}
    for node in range(0, num_nodes):
        connections = range(0, num_nodes)
        connections.remove(node)
        graph[node] = set(connections)

    return graph

def compute_in_degrees(digraph):
    """ dict -> dict
    Takes a digraph represented as a dictionary, and returns a dictionary in 
    which the keys are the nodes and the values is the node's indegree value.
    """
    indegrees = {}
    for node in digraph:
        indegrees[node] = 0
    for node in digraph:
        for edge in digraph[node]:
            indegrees[edge] += 1

    return indegrees


def in_degree_distribution(digraph):
    """ dict -> dict
    Takes a digraph dictionary object, and returns a dictionary of the degrees,
    and values being the number of nodes with that degree.
    """

    degrees = {}

    node_indegrees = compute_in_degrees(digraph)
    for node in node_indegrees:
        degree = node_indegrees[node]
        if degree in degrees:
            degrees[degree] += 1
        else:
            degrees[degree] = 1

    return degrees

