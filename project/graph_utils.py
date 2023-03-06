import pytest
import cfpq_data as cfpq
import networkx as nx


def get_graph_info(name):
    path = cfpq.download(name)
    graph = cfpq.graph_from_csv(path)

    graph_info = (
        graph.number_of_nodes(),
        graph.number_of_edges(),
        graph.edges(data=True),
    )

    return graph_info


def save_two_cycles_in_pydot(path, n, m, ls=("a", "b")):
    graph = cfpq.labeled_two_cycles_graph(n, m, labels=ls)
    nx.nx_pydot.write_dot(graph, path)
