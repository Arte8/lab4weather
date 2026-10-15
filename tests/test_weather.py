
import pytest

from weathersummary import WeatherReading


@pytest.mark.parametrize(
    "temperature, precipitation",
    [
        (10.0, 0.0),
        (15.5, 0.2),
        (20.0, 1.5),
        (-5.0, 0.0),
    ]
)
def test_valid_weather_readings(temperature, precipitation):
    reading = WeatherReading(
        "2026-10-01T12:00",
        temperature,
        precipitation
    )

    assert reading.temperature == temperature
    assert reading.precipitation == precipitation

def test_invalid_temperature_raises_error():
    with pytest.raises(
        ValueError,
        match="could not convert string to float"
    ):
        WeatherReading(
            "2026-10-01T12:00",
            "invalid",
            0.2
        )
