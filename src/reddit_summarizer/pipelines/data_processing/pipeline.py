"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.19.3
"""

from kedro.pipeline import Pipeline, pipeline, node

from .nodes import summarize_submissions


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=summarize_submissions,
                inputs=["submissions-raw", "summarization-model", "fill-mask-model"],
                outputs="submissions-summaries",
                name="summarize",
            ),
        ]
    )
