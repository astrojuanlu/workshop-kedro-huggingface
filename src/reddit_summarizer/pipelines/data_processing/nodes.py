"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.19.3
"""

import polars as pl

from .utils import get_summary, get_hashtags


def summarize_submissions(
    submissions_raw: pl.DataFrame, summarizer, mask_filler
) -> pl.DataFrame:
    """Add summaries to submissions data."""

    df = (
        submissions_raw.with_columns(
            pl.col("selftext")
            .map_elements(
                lambda text: get_summary(text, summarizer_model=summarizer),
                return_dtype=pl.Utf8,
            )
            .alias("summary"),
        )
        .with_columns(
            pl.col("summary")
            .map_elements(
                lambda text: str(get_hashtags(text, mask_filler_model=mask_filler)),
                return_dtype=pl.Utf8,
            )
            .alias("hashtags")
        )
        .with_columns(
            (
                pl.col("summary").str.len_chars() / pl.col("selftext").str.len_chars()
            ).alias("summarization_pct")
        )
        .select(
            pl.col(
                "author_name",
                "creation_datetime",
                "permalink",
                "title",
                "selftext",
                "summary",
                "hashtags",
                "summarization_pct",
            )
        )
    )

    return df
