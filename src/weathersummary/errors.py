class WeatherError(Exception):
    """Base exception for weather application."""


class WeatherAPIError(WeatherError):
    """Raised when weather API requests fail."""


class WeatherDataError(WeatherError):
    """Raised when weather data is invalid."""
