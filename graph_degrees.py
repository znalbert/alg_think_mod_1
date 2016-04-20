"""
Project 1 for Algorithmic Thinking
"""
import urllib2
import matplotlib.pyplot as plt
import random

CITATION_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_phys-cite.txt"

def load_graph(graph_url):
    """
    Function that loads a graph given the URL
    for a text representation of the graph

    Returns a dictionary that models a graph
    """
    graph_file = urllib2.urlopen(graph_url)
    graph_text = graph_file.read()
    graph_lines = graph_text.split('\n')
    graph_lines = graph_lines[ : -1]

    print "Loaded graph with", len(graph_lines), "nodes"

    answer_graph = {}
    for line in graph_lines:
        neighbors = line.split(' ')
        node = int(neighbors[0])
        answer_graph[node] = set([])
        for neighbor in neighbors[1 : -1]:
            answer_graph[node].add(int(neighbor))

    return answer_graph, len(graph_lines)

# citation_graph, total_nodes = load_graph(CITATION_URL)

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

def compute_out_degrees(digraph):
    out_degrees = {}
    for node in digraph:
        out_degrees[node] = len(digraph[node])

    return out_degrees

def avg_out_degree(out_degree_dict, num_nodes):
    total_out_degree = 0
    for node in out_degree_dict:
        total_out_degree += out_degree_dict[node]

    return float(total_out_degree)/num_nodes

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


def normalized_in_degree(in_degree_dict, num_nodes):
    normalized = {}
    for key in in_degree_dict:
        normalized[key] = float(in_degree_dict[key]) / num_nodes
    return normalized


def plot_points(plot_dict):
    x = []
    y = []
    for key in plot_dict:
        x.append(key)
        y.append(plot_dict[key])
    return x, y


class DPATrial:
    """
    Simple class to encapsulate optimized trials for DPA algorithm
    
    Maintains a list of node numbers with multiple instances of each number.
    The number of instances of each node number are
    in the same proportion as the desired probabilities
    
    Uses random.choice() to select a node number from this list for each trial.
    """

    def __init__(self, num_nodes):
        """
        Initialize a DPATrial object corresponding to a 
        complete graph with num_nodes nodes
        
        Note the initial list of node numbers has num_nodes copies of
        each node number
        """
        self._num_nodes = num_nodes
        self._node_numbers = [node for node in range(num_nodes) for dummy_idx in range(num_nodes)]


    def run_trial(self, num_nodes):
        """
        Conduct num_node trials using by applying random.choice()
        to the list of node numbers
        
        Updates the list of node numbers so that the number of instances of
        each node number is in the same ratio as the desired probabilities
        
        Returns:
        Set of nodes
        """
        
        # compute the neighbors for the newly-created node
        new_node_neighbors = set()
        for dummy_idx in range(num_nodes):
            new_node_neighbors.add(random.choice(self._node_numbers))
        
        # update the list of node numbers so that each node number 
        # appears in the correct ratio
        self._node_numbers.append(self._num_nodes)
        self._node_numbers.extend(list(new_node_neighbors))
        
        #update the number of nodes
        self._num_nodes += 1
        return new_node_neighbors


def dpa_alg(n, m):
    graph = make_complete_graph(m)
    trial = DPATrial(m)
    for i in range(m, n):
        neighbors = trial.run_trial(m)
        graph[i] = neighbors
    return graph

dpa_graph = dpa_alg(27770, 13)

dpa_in_degree = in_degree_distribution(dpa_graph)
dpa_normalized = normalized_in_degree(dpa_in_degree, 27770)

x, y = plot_points(dpa_normalized)
plt.plot(x, y, 'ro')
plt.yscale('log')
plt.xscale('log')
plt.ylabel('log(Normalized Distribution)')
plt.xlabel('log(Degree of DPA)')
plt.grid(True)
plt.title('Log/Log Normalized Distribution vs Degree of DPA')
plt.show()

