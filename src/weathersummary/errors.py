"""Custom exceptions for the weather application."""


class WeatherError(Exception):
    """Base exception for weather-related errors."""


class WeatherDownloadError(WeatherError):
    """Raised when a weather download fails."""


class WeatherDataError(WeatherError):
    """Raised when the weather data structure is invalid."""
