
import pytest

from weathersummary import WeatherReading


@pytest.fixture
def sample_readings():
    """Create hand-made weather records without using the network."""
    return [
        WeatherReading("2026-10-01T08:00", 10.0, 0.2),
        WeatherReading("2026-10-01T12:00", 20.0, 0.4),
        WeatherReading("2026-10-02T08:00", 15.0, 0.6),
    ]
