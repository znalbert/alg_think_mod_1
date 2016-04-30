"""
Assignment 1 for Algorithmic Thinking
"""
import urllib2
import matplotlib.pyplot as plt
import random
import dpa_trial as dpa
import load_graph as citations

# Also in project1.py
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


# Also in project1.py
def compute_in_degrees(digraph):
    """ dict -> dict
    Takes a digraph represented as a dictionary, and returns a dictionary in 
    which the keys are the nodes and the values are the nodes' indegree value.
    """
    indegrees = {}
    for node in digraph:
        indegrees[node] = 0
    for node in digraph:
        for edge in digraph[node]:
            indegrees[edge] += 1

    return indegrees


# Also in project1.py
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


def compute_out_degrees(digraph):
    """ dict -> dict
    Takes a directed graph represented as a dictionary, and returns a dictionary
    in which the keys are the nodes and the values are the nodes' outdegree
    value.
    """
    out_degrees = {}
    for node in digraph:
        out_degrees[node] = len(digraph[node])

    return out_degrees


def avg_out_degree(out_degree_dict):
    """ dict -> int
    Takes a dictionary of node keys and their outdegree values and an interger
    representing the number of nodes, and returns the average outdegree.
    """
    total_out_degree = 0
    for node in out_degree_dict:
        total_out_degree += out_degree_dict[node]

    return float(total_out_degree)/len(out_degree_dict)


def normalized_in_degree(in_degree_dict):
    """dict -> dict
    Takes a dictionary of nodes with their indegree value, and returns a 
    normalized dictionary whose values sum up to 1.
    """
    normalized = {}
    for key in in_degree_dict:
        normalized[key] = float(in_degree_dict[key]) / len(in_degree_dict)
    return normalized


def dpa_alg(nodes, out_degree):
    """ int, int -> dict
    Takes a number of nodes and average out-degreee of those nodes, and returns
    a dictionary representing the graph of the DPA algorithm with those values.
    """
    graph = make_complete_graph(out_degree)
    trial = dpa.DPATrial(out_degree)
    for new_node in range(out_degree, nodes):
        neighbors = trial.run_trial(out_degree)
        graph[new_node] = neighbors
    return graph


def plot_points(plot_dict):
    """ dict -> list, list
    Takes a dictionary and returns the key-value pairs as x and y lists to be 
    plotted.
    """
    x = []
    y = []
    for key in plot_dict:
        x.append(key)
        y.append(plot_dict[key])
    return x, y


def plot_loglog_norm_dist_vs_dpa_deg(nodes, out_degree):
    """ int, int -> graph
    Takes a number of nodes and avgerage outdegree for them, and returns a 
    the Log/Log plot of the normalized distribution vs node degree of the 
    DPA algorithm.
    """
    dpa_graph = dpa_alg(nodes, out_degree)
    dpa_in_degree = in_degree_distribution(dpa_graph)
    dpa_normalized = normalized_in_degree(dpa_in_degree)

    x, y = plot_points(dpa_normalized)
    plt.plot(x, y, 'ro')
    plt.yscale('log')
    plt.xscale('log')
    plt.ylabel('log(Normalized Distribution)')
    plt.xlabel('log(Degree of DPA)')
    plt.grid(True)
    plt.title('Log/Log Normalized Distribution vs Degree of DPA')
    plt.show()

# plot_loglog_norm_dist_vs_dpa_deg(27770, 13)
