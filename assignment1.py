"""
Algorithmic Thinking - Assignment 1
"""

import matplotlib.pyplot as plt


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

