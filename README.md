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

cd lab4weather

conda env create -f environment.yml

conda activate module04-quality

python -m pip install -r requirements.txt

python -m pip install -e .
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
## Settings
weather.latitude
Sets the latitude of the location used to retrieve weather data (43.65 for Toronto).

weather.longitude
Sets the longitude of the location used to retrieve weather data (-79.38 for Toronto).

weather.hourly
Specifies which hourly weather variables to download, including temperature and precipitation.

weather.past_days
Determines how many previous days of weather data to retrieve (7 days).

weather.forecast_days
Determines how many future forecast days to request (0 days).

weather.timezone
Sets the timezone used for weather timestamps (America/Toronto).

network.timeout
Sets the maximum number of seconds to wait for an API response (15 seconds).

output.path
Specifies where the processed weather summary JSON file is saved (data/processed/summary.json).

The application downloads and processes the weather data, displays statistics, and writes the summary to:
`data/processed/summary.json`

An internet connection is required for live weather downloads.

## Errors and Exit Codes

| Error class | When it is raised | What the user sees |
|---|---|---|
| `WeatherDownloadError` | The weather API request fails or times out. | The download error message. |
| `WeatherDataError` | The downloaded weather data is invalid or cannot be processed. | `Weather data error:` followed by the error details. |
| `ValueError`, `KeyError`, `TypeError` | Data contains invalid values, missing keys, or incorrect types. | `Weather data error:` followed by the error details. |
| `OSError` | The application cannot save the JSON output files. | `Unable to save the JSON file:` followed by the error details. |

### Exit Codes

| Exit code | Meaning |
|---|---|
| `0` | Success — the application completed and saved its output files. |
| `1` | Failure — a download, validation, processing, or file-saving error occurred, or fewer than 50 required records were available. |

## Reproducing a Run

The Weather Summary application does not use random sampling, so no random seed is required.

The `config/settings.toml` file stores the weather location, requested variables, date range, timezone, network timeout, and output path.

The `data/processed/run_info.json` file records:

- Execution timestamp in UTC.
- Number of records downloaded.
- Number of valid records processed.
- Number of rejected records.

To reproduce a run, a classmate needs the same project code, Python dependencies, TOML configuration, and weather data returned by the Open-Meteo API.

Because Open-Meteo returns weather data based on the requested dates, running the application at a different time may produce different results. Reproducing the exact same summary requires using the same original API response or an archived copy of the input data.

The application saves its calculated weather statistics in `data/processed/summary.json`.

## What the Tests Cover

The automated tests help protect the following application behaviours:

- **Data validation:** Weather readings must contain valid timestamps, temperatures, and precipitation values.
- **Invalid records:** Invalid weather readings are rejected without preventing valid records from being processed.
- **Weather calculations:** Temperature and precipitation statistics are calculated correctly.
- **Daily aggregation:** Weather readings are grouped by date to produce daily statistics.
- **Error handling:** Invalid data and download failures are handled appropriately.
- **Output consistency:** Weather summaries contain the expected information and record counts.

**What was not tested:** Live Open-Meteo API availability was intentionally excluded from the automated tests because it depends on an external service and internet connectivity. Offline tests are more reliable and produce consistent results without network access.

## Known Limitations

- **Internet dependency:** The application requires an internet connection to retrieve weather data from the Open-Meteo API.
- **Limited historical data:** The application currently retrieves the previous seven days of weather data, as configured in `settings.toml`.
- **Changing results:** Weather data may differ between runs because the application uses a rolling date range.
- **Minimum record requirement:** The application stops with exit code `1` if fewer than 50 records are downloaded or fewer than 50 valid readings remain.
- **Limited error recovery:** The application reports download failures but does not automatically retry unsuccessful API requests.
- **No graphical interface:** Results are displayed in the terminal and saved as JSON files.

### Future Improvements

With more development time, I would add automatic retries for API failures, support fixed date ranges for reproducible results, and provide graphical visualizations of temperature and precipitation trends.

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

