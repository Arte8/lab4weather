"""Build and save the weather summary."""

import json

from .aggregations import (
    DailyStatistics,
    OverallStatistics,
    UniqueDates,
)
from .config import OUTPUT_PATH


def create_summary(url, readings, downloaded, rejected):
    """Build a summary using the original Lab 02 keys."""

    summary = {
        "source_url": url,
        "records_downloaded": downloaded,
        "records_processed": len(readings),
        "records_rejected": rejected,
    }

    aggregations = [
        UniqueDates(),
        OverallStatistics(),
        DailyStatistics(),
    ]

    # Polymorphism: call the overridden method on each object.
    for aggregation in aggregations:
        summary[aggregation.key] = aggregation.compute(readings)

    return summary


def save_summary(summary):
    """Write the summary to the configured JSON output path."""

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    with OUTPUT_PATH.open("w", encoding="utf-8") as file:
        json.dump(summary, file, indent=2, allow_nan=False)

    return OUTPUT_PATH
