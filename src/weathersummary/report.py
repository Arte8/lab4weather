"""Build and save the weather summary."""

import json
from pathlib import Path
from typing import Any

from .aggregations import (
    DailyStatistics,
    OverallStatistics,
    UniqueDates,
)
from .config import OUTPUT_PATH
from .models import WeatherReading


def create_summary(
    url: str,
    readings: list[WeatherReading],
    downloaded: int,
    rejected: int,
) -> dict[str, Any]:
    """Build a summary using the original Lab 02 keys."""

    summary: dict[str, Any] = {
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


def save_summary(summary: dict[str, Any]) -> Path:
    """Write the summary to the configured JSON output path."""

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    with OUTPUT_PATH.open("w", encoding="utf-8") as file:
        json.dump(summary, file, indent=2, allow_nan=False)

    return OUTPUT_PATH


def save_run_info(
    downloaded: int,
    processed: int,
    rejected: int,
) -> Path:
    """Save execution information to a JSON file."""

    from datetime import UTC, datetime

    run_info_path = OUTPUT_PATH.parent / "run_info.json"

    run_info = {
        "timestamp": datetime.now(UTC).isoformat(),
        "records_downloaded": downloaded,
        "records_processed": processed,
        "records_rejected": rejected,
    }

    run_info_path.parent.mkdir(parents=True, exist_ok=True)

    with run_info_path.open("w", encoding="utf-8") as file:
        json.dump(run_info, file, indent=2)

    return run_info_path
