"""Convert raw weather data into validated reading objects."""

from .models import WeatherReading


def process_weather(data):
    """Return valid readings, downloaded count, and rejected count."""

    hourly = data["hourly"]

    times = hourly["time"]
    temperatures = hourly["temperature_2m"]
    precipitation = hourly["precipitation"]

    if not (
        len(times) == len(temperatures) == len(precipitation)
    ):
        raise ValueError(
            "Weather data arrays have different lengths."
        )

    readings = []
    rejected = 0

    for time, temperature, rainfall in zip(
        times, temperatures, precipitation
    ):
        try:
            reading = WeatherReading(
                time,
                temperature,
                rainfall
            )

            readings.append(reading)

        except (ValueError, TypeError, OverflowError):
            rejected += 1

    return readings, len(times), rejected