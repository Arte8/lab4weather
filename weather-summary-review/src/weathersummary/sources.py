"""Download weather data and return validated reading objects."""

import requests

from .config import URL, TIMEOUT
from .processing import process_weather


class WeatherDownloadError(Exception):
    """Represent a failed weather download."""


class WeatherSource:
    """Fetch weather data and convert it into WeatherReading objects."""

    def __init__(self, url=URL, timeout=TIMEOUT):
        self.url = url
        self.timeout = timeout

    def download(self):
        """Return readings, downloaded count, and rejected count."""

        try:
            response = requests.get(
                self.url,
                timeout=self.timeout
            )
            response.raise_for_status()
            data = response.json()

        except requests.RequestException as error:
            raise WeatherDownloadError(
                f"Weather download failed: {error}"
            ) from error

        return process_weather(data)