
import pytest

from weathersummary.errors import (
    WeatherError,
    WeatherAPIError,
    WeatherDataError,
)


def test_weather_api_error():
    with pytest.raises(WeatherError, match="API unavailable"):
        raise WeatherAPIError("API unavailable")


def test_weather_data_error():
    with pytest.raises(WeatherError, match="Invalid weather data"):
        raise WeatherDataError("Invalid weather data")

