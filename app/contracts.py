from datetime import UTC, datetime
from enum import StrEnum
from uuid import UUID, uuid4

from pydantic import BaseModel, ConfigDict, Field


def utc_now() -> datetime:
    return datetime.now(UTC)


class EvaluationStatus(StrEnum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    PARTIAL = "partial"


class EvaluationExample(BaseModel):
    """A single input example in an evaluation dataset."""

    example_id: str
    question: str
    context: str
    expected_answer: str


class EvaluationRun(BaseModel):
    """Metadata describing one evaluation experiment."""

    run_id: UUID = Field(default_factory=uuid4)

    dataset_name: str
    dataset_version: str

    model_name: str
    prompt_version: str
    evaluator_version: str

    git_commit: str | None = None

    status: EvaluationStatus = EvaluationStatus.PENDING

    sample_count: int = 0

    started_at: datetime = Field(default_factory=utc_now)
    completed_at: datetime | None = None


class EvaluatorResult(BaseModel):
    """Individual evaluator output for one example."""

    model_config = ConfigDict(use_enum_values=True)

    result_id: UUID = Field(default_factory=uuid4)

    run_id: UUID
    example_id: str

    evaluator_name: str
    evaluator_version: str

    score: float = Field(ge=0.0, le=1.0)
    passed: bool

    explanation: str | None = None

    evaluated_at: datetime = Field(default_factory=utc_now)


class MetricObservation(BaseModel):
    """An aggregated metric observation for monitoring."""

    observation_id: UUID = Field(default_factory=uuid4)

    run_id: UUID

    metric_name: str
    metric_value: float

    sample_count: int = Field(ge=1)

    model_name: str
    prompt_version: str

    observed_at: datetime = Field(default_factory=utc_now)
