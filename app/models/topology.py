from pydantic import BaseModel
from typing import List, Optional

class Service(BaseModel):
    name: str
    criticality: int  # 1-5
    cost_per_minute: float
    slo_target: float  # e.g. 99.9
    dependencies: List[str] = []

class Topology(BaseModel):
    services: List[Service]