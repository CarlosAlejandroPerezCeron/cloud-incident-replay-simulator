import networkx as nx
from app.models.topology import Topology

def build_graph(topology: Topology) -> nx.DiGraph:
    graph = nx.DiGraph()

    for service in topology.services:
        graph.add_node(
            service.name,
            criticality=service.criticality,
            cost_per_minute=service.cost_per_minute,
            slo_target=service.slo_target,
        )

        for dep in service.dependencies:
            graph.add_edge(service.name, dep)

    return graph
