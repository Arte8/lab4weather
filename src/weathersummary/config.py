"""Central settings for the weather summary application."""

import tomllib
from pathlib import Path
from urllib.parse import urlencode

# Locate the Lab 04 project root
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# Load settings from TOML
SETTINGS_PATH = PROJECT_ROOT / "config" / "settings.toml"

with SETTINGS_PATH.open("rb") as file:
    settings = tomllib.load(file)

# Weather settings
weather = settings["weather"]
network = settings["network"]
output = settings["output"]

# Build the Open-Meteo API URL
URL = "https://api.open-meteo.com/v1/forecast?" + urlencode(
    {
        "latitude": weather["latitude"],
        "longitude": weather["longitude"],
        "hourly": weather["hourly"],
        "past_days": weather["past_days"],
        "forecast_days": weather["forecast_days"],
        "timezone": weather["timezone"],
    }
)

# Network timeout
TIMEOUT = network["timeout"]

# Output path
OUTPUT_PATH: Path = PROJECT_ROOT / str(output["path"])
