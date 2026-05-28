from fastapi import APIRouter
from app.models.topology import Topology
from app.models.simulation import FailureScenario
from app.graph.builder import build_graph
from app.simulation.engine import propagate_failure
from app.simulation.impact import calculate_financial_impact, calculate_blast_radius_score

router = APIRouter()

@router.post("/simulate")
def simulate(topology: Topology, scenario: FailureScenario):
    graph = build_graph(topology)
    impacted = propagate_failure(graph, scenario.failed_node)

    financial_loss = calculate_financial_impact(
        graph, impacted, scenario.duration_minutes
    )

    blast_score = calculate_blast_radius_score(graph, impacted)

    return {
        "failed_node": scenario.failed_node,
        "impacted_services": impacted,
        "financial_loss_estimate": financial_loss,
        "blast_radius_score": blast_score
    }