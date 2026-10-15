"""Represent and validate a single hourly weather reading."""

import math

import pandas as pd


class WeatherReading:
    """Store one weather reading, cleaning its values during creation."""

    def __init__(
        self,
        time: str,
        temperature: float,
        precipitation: float,
    ) -> None:
        self.time = pd.to_datetime(time, errors="raise")

        if pd.isna(self.time):
            raise ValueError("Missing timestamp")

        self.temperature = float(temperature)
        self.precipitation = float(precipitation)

        if not (math.isfinite(self.temperature) and math.isfinite(self.precipitation)):
            raise ValueError("Missing or non-finite value")

        if self.precipitation < 0:
            raise ValueError("Negative precipitation")

    def __str__(self) -> str:
        return (
            f"{self.time.isoformat()}: "
            f"{self.temperature} °C, "
            f"{self.precipitation} mm precipitation"
        )
