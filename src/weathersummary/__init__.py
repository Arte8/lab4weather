"""Public classes and functions for the weather summary package."""

from .aggregations import (
    Aggregation,
    DailyStatistics,
    OverallStatistics,
    UniqueDates,
)
from .models import WeatherReading
from .processing import process_weather
from .report import create_summary, save_summary
from .sources import WeatherDownloadError, WeatherSource

__all__ = [
    "Aggregation",
    "DailyStatistics",
    "OverallStatistics",
    "UniqueDates",
    "WeatherDownloadError",
    "WeatherReading",
    "WeatherSource",
    "create_summary",
    "process_weather",
    "save_summary",
]
