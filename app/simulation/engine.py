import networkx as nx
from typing import List

def propagate_failure(graph: nx.DiGraph, failed_node: str) -> List[str]:
    impacted = set()
    impacted.add(failed_node)

    for node in nx.descendants(graph, failed_node):
        impacted.add(node)

    return list(impacted)