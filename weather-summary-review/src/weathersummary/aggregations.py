"""Calculate weather statistics through a shared aggregation interface."""

from abc import ABC, abstractmethod
from collections import defaultdict

import pandas as pd


class Aggregation(ABC):
    """Define the common interface for weather aggregations."""

    @abstractmethod
    def compute(self, readings):
        """Calculate a result from validated weather readings."""
        pass


class OverallStatistics(Aggregation):
    """Calculate overall temperature and precipitation statistics."""

    key = "overall_statistics"

    def compute(self, readings):
        # Use pandas to preserve the original Lab 02 calculations.
        df = pd.DataFrame(
            [
                (reading.temperature, reading.precipitation)
                for reading in readings
            ],
            columns=["temperature", "precipitation"]
        )

        return {
            "minimum_temperature": float(df["temperature"].min()),
            "maximum_temperature": float(df["temperature"].max()),
            "mean_temperature": float(df["temperature"].mean()),
            "minimum_precipitation": float(df["precipitation"].min()),
            "maximum_precipitation": float(df["precipitation"].max()),
            "mean_precipitation": float(df["precipitation"].mean()),
            "total_precipitation": float(df["precipitation"].sum())
        }


class DailyStatistics(Aggregation):
    """Calculate average temperature and total precipitation per day."""

    key = "daily_statistics"

    def compute(self, readings):
        daily_records = defaultdict(list)

        for reading in readings:
            date = reading.time.date().isoformat()

            daily_records[date].append(
                (reading.temperature, reading.precipitation)
            )

        return {
            date: {
                "average_temperature": sum(
                    record[0] for record in records
                ) / len(records),

                "total_precipitation": sum(
                    record[1] for record in records
                ),

                "record_count": len(records)
            }
            for date, records in daily_records.items()
        }


class UniqueDates(Aggregation):
    """Collect the distinct dates in chronological order."""

    key = "unique_dates"

    def compute(self, readings):
        return sorted({
            reading.time.date().isoformat()
            for reading in readings
        })