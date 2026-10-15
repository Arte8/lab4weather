class WeatherError(Exception):
    """Base exception for weather application."""
    pass


class WeatherAPIError(WeatherError):
    """Raised when weather API requests fail."""
    pass


class WeatherDataError(WeatherError):
    """Raised when weather data is invalid."""
    pass