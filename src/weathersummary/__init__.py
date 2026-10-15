"""Public classes and functions for the weather summary package."""

from .models import WeatherReading
from .sources import WeatherSource, WeatherDownloadError
from .aggregations import (
    Aggregation,
    OverallStatistics,
    DailyStatistics,
    UniqueDates,
)
from .processing import process_weather
from .report import create_summary, save_summary

__all__ = [
    "WeatherReading",
    "WeatherSource",
    "WeatherDownloadError",
    "Aggregation",
    "OverallStatistics",
    "DailyStatistics",
    "UniqueDates",
    "process_weather",
    "create_summary",
    "save_summary",
]