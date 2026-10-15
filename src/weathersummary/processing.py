"""Convert raw weather data into validated reading objects."""

import logging

from .errors import WeatherDataError
from .models import WeatherReading

logger = logging.getLogger(__name__)


def process_weather(data):
    """Return valid readings, downloaded count, and rejected count."""

    try:
        hourly = data["hourly"]

        times = hourly["time"]
        temperatures = hourly["temperature_2m"]
        precipitation = hourly["precipitation"]

    except (KeyError, TypeError) as error:
        raise WeatherDataError("Missing or invalid weather data fields.") from error

    if not (len(times) == len(temperatures) == len(precipitation)):
        raise WeatherDataError("Weather data arrays have different lengths.")

    readings = []
    rejected = 0

    for time, temperature, rainfall in zip(times, temperatures, precipitation):
        try:
            reading = WeatherReading(time, temperature, rainfall)

            readings.append(reading)

        except (ValueError, TypeError, OverflowError):
            rejected += 1
            logger.warning("Rejected invalid weather record")

    logger.info("Processed %s records; rejected %s", len(readings), rejected)

    return readings, len(times), rejected
