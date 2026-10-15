"""Run the weather download, processing, and reporting workflow."""

from weathersummary import (
    WeatherSource,
    WeatherDownloadError,
    process_weather,
    create_summary,
    save_summary,
)
from weathersummary.config import URL


def main():
    """Run the application and display clear error messages."""

    try:
        readings, downloaded, rejected = WeatherSource().download()


        if downloaded < 50:
            print("Error: Fewer than 50 records downloaded.")
            return 1

        if len(readings) < 50:
            print("Error: Fewer than 50 valid records available.")
            print("Rejected records:", rejected)
            return 1

        summary = create_summary(
            URL, readings, downloaded, rejected
        )

        stats = summary["overall_statistics"]

        print("Minimum temperature:",
              stats["minimum_temperature"], "°C")
        print("Maximum temperature:",
              stats["maximum_temperature"], "°C")
        print("Mean temperature:",
              stats["mean_temperature"], "°C")

        print("Minimum precipitation:",
              stats["minimum_precipitation"], "mm")
        print("Maximum precipitation:",
              stats["maximum_precipitation"], "mm")
        print("Mean precipitation:",
              stats["mean_precipitation"], "mm")

        print("\nDaily statistics:")

        for date, values in summary["daily_statistics"].items():
            print(date, values)

        output_file = save_summary(summary)

        print("\nRecords downloaded:", downloaded)
        print("Records processed:", len(readings))
        print("Records rejected:", rejected)
        print("Summary saved to:", output_file)

        return 0

    except WeatherDownloadError as error:
        print(error)

    except (ValueError, KeyError, TypeError) as error:
        print("Weather data error:", error)

    except OSError as error:
        print("Unable to save the JSON file:", error)

    return 1


if __name__ == "__main__":
    raise SystemExit(main())