from pydantic import BaseModel

class FailureScenario(BaseModel):
    failed_node: str
    duration_minutes: int
