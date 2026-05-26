def calculate_financial_impact(graph, impacted_nodes, duration):
    total_loss = 0

    for node in impacted_nodes:
        cost = graph.nodes[node].get("cost_per_minute", 0)
        total_loss += cost * duration

    return total_loss


def calculate_blast_radius_score(graph, impacted_nodes):
    score = 0

    for node in impacted_nodes:
        criticality = graph.nodes[node].get("criticality", 1)
        score += criticality

    return score
