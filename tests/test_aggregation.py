
import pytest

from weathersummary.aggregations import (
    OverallStatistics,
    DailyStatistics,
    UniqueDates,
)


def test_overall_statistics(sample_readings):
    result = OverallStatistics().compute(sample_readings)

    assert result["minimum_temperature"] == 10.0
    assert result["maximum_temperature"] == 20.0
    assert result["mean_temperature"] == pytest.approx(15.0)
    assert result["total_precipitation"] == pytest.approx(1.2)


def test_daily_statistics(sample_readings):
    result = DailyStatistics().compute(sample_readings)

    assert result["2026-10-01"]["average_temperature"] == 15.0
    assert result["2026-10-01"]["total_precipitation"] == pytest.approx(0.6)
    assert result["2026-10-01"]["record_count"] == 2

    assert result["2026-10-02"]["average_temperature"] == 15.0
    assert result["2026-10-02"]["record_count"] == 1


def test_unique_dates(sample_readings):
    result = UniqueDates().compute(sample_readings)

    assert result == [
        "2026-10-01",
        "2026-10-02",
    ]
