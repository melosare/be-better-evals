# be-better-evals

An LLM evaluation, observability, and regression detection platform.

## Objectives

- Multi-dimensional LLM evaluation
- Versioned evaluation experiments
- Historical quality monitoring
- Regression detection
- Automated email alerting
- Interactive Plotly Dash dashboard

## Technology Stack

- Python 3.11
- Pydantic
- SQLAlchemy
- Plotly Dash
- Pandas
- OpenAI API
- Pytest

## Development

Activate the Conda environment:

    conda activate be-better-evals

Install dependencies:

    pip install -r requirements.txt

Run tests:

    python -m pytest

Run linting:

    ruff check app tests
