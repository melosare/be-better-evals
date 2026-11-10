from uuid import UUID

from app.contracts import (
    EvaluationExample,
    EvaluationRun,
    EvaluationStatus,
    EvaluatorResult,
    MetricObservation,
)


def test_evaluation_example_creation():
    example = EvaluationExample(
        example_id="test-001",
        question="What is the refund policy?",
        context="Customers can request refunds within 30 days.",
        expected_answer="Refunds are available within 30 days.",
    )

    assert example.example_id == "test-001"


def test_evaluation_run_creation():
    run = EvaluationRun(
        dataset_name="customer-support",
        dataset_version="v1",
        model_name="test-model",
        prompt_version="v1",
        evaluator_version="1.0.0",
    )

    assert isinstance(run.run_id, UUID)
    assert run.status == EvaluationStatus.PENDING


def test_evaluator_result_score_validation():
    result = EvaluatorResult(
        run_id=UUID("00000000-0000-0000-0000-000000000001"),
        example_id="test-001",
        evaluator_name="groundedness",
        evaluator_version="1.0.0",
        score=0.95,
        passed=True,
    )

    assert result.score == 0.95


def test_metric_observation_creation():
    observation = MetricObservation(
        run_id=UUID("00000000-0000-0000-0000-000000000001"),
        metric_name="groundedness",
        metric_value=0.92,
        sample_count=100,
        model_name="test-model",
        prompt_version="v1",
    )

    assert observation.sample_count == 100
    assert observation.metric_value == 0.92
