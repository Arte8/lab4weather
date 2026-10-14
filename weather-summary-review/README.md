Weather summary lab3

This project downloads Toronto hourly weather data from Open-Meteo, validates each reading, calculates statistics, and saves a JSON summary.

Open Anaconda Prompt in the repository folder:
clone into new folder 

**git clone https://github.com/ARTE8/lab3weather.git weather-summary-review**

**cd weather-summary-review**   or root folder

**conda env create -n weather-summary-review -f environment.yml**

**conda activate weather-summary-review**

**python -m pip install -e .**

**python main.py**

```

The editable installation allows importing `weathersummary` without
changing `sys.path`.


Internet access is required for downloading weather data.
The output is saved to `data/processed/summary.json`.

At least 50 downloaded records and 50 valid readings are required.
Download failures print a clear message and exit without a traceback.

With the environment activated, run:

```cmd
python -m unittest discover -s tests
```

The tests use hand-made records and do not access the network.
They check numeric conversion, rejection of invalid values, and the record's string representation.


- `config.py`: source URL, request timeout, and relative output path. - `models.py`: `WeatherReading`, which validates values in `__init__`. - `sources.py`: `WeatherSource`, which returns reading objects and counts.
  This is the only module importing `requests`.
- `processing.py`: constructs readings and counts rejected records.
- `aggregations.py`: the `Aggregation` base class and subclasses.
- `report.py`: builds the summary and writes JSON.
- `__init__.py`: re-exports the public classes and functions.
- `main.py`: connects the components and prints results or errors.

- | Lab 02 function | Where the code lives now |
|---|---|
| `download_weather(url)` | `sources.py`: `WeatherSource.download()` |
| `process_weather(data)` | Record-value validation moved to `models.py`: `WeatherReading.__init__()`. Array-length checks, reading construction, and record counts remain in `processing.py`: `process_weather()`. |
| `calculate_statistics(df)` | `aggregations.py`: `OverallStatistics.compute(readings)` |
| `calculate_daily_statistics(df)` | `aggregations.py`: `DailyStatistics.compute(readings)` |
| `get_unique_dates(df)` | `aggregations.py`: `UniqueDates.compute(readings)` |
| `create_summary(url, df, downloaded, rejected)` | `report.py`: `create_summary(url, readings, downloaded, rejected)` |
| `save_summary(summary)` | `report.py`: `save_summary(summary)` |
| `main()` | Root `main.py`: `main()`, which coordinates the modules and prints messages. |

Classes and responsibilities

`WeatherReading` represents one hourly weather record. Its explicit
`__init__()` converts timestamps and numeric values and rejects missing,
malformed, non-finite, or negative precipitation values. Centralizing
these checks applies the same validation whenever a reading is created.
Its `__str__()` method provides a readable description.

`WeatherSource` handles downloading. Its explicit `__init__()` stores
the URL and timeout. Its `download()` method retrieves the API response
and calls the processing function, returning reading objects and record
counts rather than raw dictionaries.

`WeatherDownloadError` represents retrieval failures. It allows
`main.py` to handle these failures without importing `requests`.

`WeatherReading` represents one hourly record and defines `__str__`.
`WeatherSource` handles retrieval. Both have an explicit `__init__`
method and a class docstring.

`OverallStatistics`, `DailyStatistics`, and `UniqueDates` inherit from
`Aggregation` and override `compute()`.

Preserving Lab 02 behaviour

The summary retains the original keys and calculations. Overall
statistics continue to use pandas, and daily statistics retain the
original grouping and arithmetic.

The application still requires at least 50 downloaded records and
50 valid readings. Download failures print a clear message and exit
without a traceback.

The summary builder loops over aggregation objects and calls their `compute()` methods without checking their subclasses.


`environment.yml` specifies the Conda environment, Python, and pip.
`requirements.txt` pins requests, pandas, and NumPy.
`pyproject.toml` declares the package dependencies and src layout.


The refactor retains the original summary keys, validation rules,
statistics, and minimum-record checks.

Known limitations

- Internet access and an available Open-Meteo service are required.
  Failed downloads are reported, but automatic retries are not implemented.
- The location and weather variables are fixed in configuration.
  Command-line options would make the application more flexible.
- Invalid readings are counted and skipped, but their individual
  rejection reasons are not saved.
- Live API data can change between runs. A meaningful Lab 02 comparison
  requires both versions to process the same saved response.
- The relative output path assumes execution from the application root.
- Successful runs overwrite `data/processed/summary.json`.
- The current tests cover record validation and representation.
  Additional tests could check aggregations, report writing, and
  download-error handling.
- Pinned dependencies improve repeatability, but they do not guarantee
  identical operating systems or external API responses.
  
To verify equivalent results, run both versions using the same saved
API response and compare the parsed JSON summaries. Separate live
downloads may contain different weather data.


enjoy
and give Art good grades!
