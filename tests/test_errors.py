import pytest

from weathersummary.errors import (
    WeatherDataError,
    WeatherDownloadError,
    WeatherError,
)
from weathersummary.processing import process_weather


def test_weather_download_error():
    with pytest.raises(WeatherError, match="API unavailable"):
        raise WeatherDownloadError("API unavailable")


def test_weather_data_error():
    with pytest.raises(WeatherError, match="Invalid weather data"):
        raise WeatherDataError("Invalid weather data")


def test_missing_weather_fields():
    with pytest.raises(
        WeatherDataError, match="Missing or invalid weather data fields"
    ):
        process_weather({})


def test_mismatched_weather_arrays():
    data = {
        "hourly": {
            "time": ["2026-10-01T12:00"],
            "temperature_2m": [18.5, 20.0],
            "precipitation": [0.2],
        }
    }

    with pytest.raises(WeatherDataError, match="different lengths"):
        process_weather(data)


def test_weather_error_inheritance():
    assert issubclass(WeatherDownloadError, WeatherError)
    assert issubclass(WeatherDataError, WeatherError)
