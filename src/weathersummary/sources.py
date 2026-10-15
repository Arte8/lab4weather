"""Download weather data and return validated reading objects."""

import logging

import requests

from .config import TIMEOUT, URL
from .errors import WeatherDownloadError
from .processing import process_weather

logger = logging.getLogger(__name__)


class WeatherSource:
    """Fetch weather data and convert it into WeatherReading objects."""

    def __init__(self, url=URL, timeout=TIMEOUT):
        self.url = url
        self.timeout = timeout

    def download(self):
        """Return readings, downloaded count, and rejected count."""

        try:
            logger.info("Downloading weather data")

            response = requests.get(self.url, timeout=self.timeout)
            response.raise_for_status()
            data = response.json()

        except requests.RequestException as error:
            logger.error("Weather download failed: %s", error)

            raise WeatherDownloadError(f"Weather download failed: {error}") from error

        return process_weather(data)
