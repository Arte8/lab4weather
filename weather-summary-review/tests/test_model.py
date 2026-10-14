"""Test weather readings using hand-made data and no network."""

import unittest

from weathersummary import WeatherReading


class TestWeatherReading(unittest.TestCase):

    def test_valid_reading_cleans_numeric_strings(self):
        reading = WeatherReading(
            "2026-10-01T12:00",
            "18.5",
            "0.2"
        )

        self.assertEqual(reading.temperature, 18.5)
        self.assertEqual(reading.precipitation, 0.2)
        self.assertEqual(
            reading.time.isoformat(),
            "2026-10-01T12:00:00"
        )

    def test_invalid_values_are_rejected(self):
        invalid_records = [
            ("not-a-date", 18.5, 0.2),
            (None, 18.5, 0.2),
            ("2026-10-01T12:00", None, 0.2),
            ("2026-10-01T12:00", "invalid", 0.2),
            ("2026-10-01T12:00", float("inf"), 0.2),
            ("2026-10-01T12:00", 18.5, -0.2),
        ]

        for values in invalid_records:
            with self.subTest(values=values):
                with self.assertRaises(
                    (ValueError, TypeError, OverflowError)
                ):
                    WeatherReading(*values)

    def test_string_representation(self):
        reading = WeatherReading(
            "2026-10-01T12:00",
            18.5,
            0.2
        )

        self.assertEqual(
            str(reading),
            "2026-10-01T12:00:00: "
            "18.5 °C, 0.2 mm precipitation"
        )


if __name__ == "__main__":
    unittest.main()