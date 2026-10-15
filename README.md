# Weather Summary — Lab 04 Software Quality

**Humber College AI511**

## Project Overview

This Python application downloads hourly Toronto weather data from the Open-Meteo API, validates individual weather readings, calculates overall and daily statistics, and saves the results as a JSON summary.

Lab 04 builds on the Lab 03 object-oriented weather application by introducing automated testing, custom exception handling, logging, static type checking, linting, formatting, and centralized tool configuration.

## Data Source

**API:** https://open-meteo.com/

Each record represents one hour of weather observations or historical model data, including:

- Timestamp
- Temperature in degrees Celsius
- Precipitation in millimetres

The application requires at least 50 downloaded records and 50 valid readings to generate a summary.

## Installation and Setup

Open Anaconda Prompt and navigate to the directory where you want to download the project:
```
Clone the Lab 04 repository from GitHub:
```
git clone https://github.com/Arte8/lab4weather
```
Navigate into the cloned project folder:
```
cd cd lab4weather
```
Create the Lab 04 Conda environment using the project's environment file:
```
conda env create -f environment.yml
```
Activate the environment specified in environment.yml. 
```
conda activate weather-lab3
```
Install the application in editable mode:
```
python -m pip install -e .
```
Install any development dependencies not already included in the environment:
```
python -m pip install pytest ruff mypy pandas-stubs types-requests
```
Execute the weather summary application:
```
python main.py
```
An internet connection is required to download weather data from Open-Meteo.
Run the automated tests:
```
python -m pytest
```
Check code quality with Ruff:
```
python -m ruff check src\weathersummary main.py tests
```
Verify code formatting:
```
python -m ruff format --check src\weathersummary main.py tests
```
Perform static type checking:
```
python -m mypy
``` 
## Running the Application

From the project root:

```cmd
python main.py
```

The application downloads and processes the weather data, displays statistics, and writes the summary to:

`data/processed/summary.json`

An internet connection is required for live weather downloads.

## Project Structure

| File | Responsibility |
|---|---|
| `main.py` | Coordinates the application workflow and handles user-facing errors |
| `src/weathersummary/config.py` | API URL, timeout, and output configuration |
| `src/weathersummary/models.py` | Defines and validates individual weather readings |
| `src/weathersummary/sources.py` | Downloads weather data and handles request failures |
| `src/weathersummary/processing.py` | Processes API records and counts rejected readings |
| `src/weathersummary/aggregations.py` | Calculates overall statistics, daily statistics, and unique dates |
| `src/weathersummary/report.py` | Creates the summary and saves JSON output |
| `src/weathersummary/errors.py` | Defines custom weather application exceptions |
| `src/weathersummary/logging_config.py` | Configures application logging |
| `src/weathersummary/__init__.py` | Exposes the package's public interfaces |
| `tests/` | Contains automated tests and shared test fixtures |
| `pyproject.toml` | Package metadata, dependencies, and development tool configuration |
| `environment.yml` | Conda environment configuration |
| `requirements.txt` | Python dependency requirements |

## Changes from Lab 02 and Lab 03

| Original function or feature | Current implementation |
|---|---|
| `download_weather(url)` | `WeatherSource.download()` in `sources.py` |
| `process_weather(data)` | `process_weather()` in `processing.py`, with individual record validation in `WeatherReading` |
| Overall statistics | `OverallStatistics.compute()` |
| Daily statistics | `DailyStatistics.compute()` |
| Unique dates | `UniqueDates.compute()` |
| `create_summary()` | `report.py` |
| `save_summary()` | `report.py` |
| `main()` | Root `main.py` |
| Download error handling | `WeatherDownloadError` in `errors.py` |
| Invalid data handling | `WeatherDataError` in `errors.py` |
| Application logging | `logging_config.py` and module-specific loggers |
| Automated quality checks | pytest, Ruff, and mypy |

## Object-Oriented Design

**WeatherReading** represents one hourly weather record. Its constructor validates timestamps, temperature, and precipitation values. Invalid numeric values and negative precipitation are rejected.

**WeatherSource** is responsible for retrieving API data and passing it to the processing module. Its constructor stores the API URL and request timeout.

**Aggregation** is an abstract base class that defines the `compute()` interface.

Three subclasses implement specialized calculations:

- `OverallStatistics`: Overall temperature and precipitation statistics
- `DailyStatistics`: Daily averages, precipitation totals, and record counts
- `UniqueDates`: Sorted unique dates in the dataset

This design uses inheritance and polymorphism. Additional aggregation types can be introduced by creating another subclass of `Aggregation` and implementing `compute()`.

