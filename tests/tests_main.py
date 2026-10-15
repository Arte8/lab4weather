
import main


def test_main_insufficient_downloads(monkeypatch, capsys):
    # Simulate fewer than 50 downloaded records
    monkeypatch.setattr(
        main.WeatherSource,
        "download",
        lambda self: ([], 10, 0)
    )

    result = main.main()
    output = capsys.readouterr().out

    assert result == 1
    assert "Fewer than 50 records downloaded" in output


def test_main_insufficient_valid_records(monkeypatch, capsys):
    # Simulate 60 downloads but no valid records
    monkeypatch.setattr(
        main.WeatherSource,
        "download",
        lambda self: ([], 60, 60)
    )

    result = main.main()
    output = capsys.readouterr().out

    assert result == 1
    assert "Fewer than 50 valid records available" in output
    assert "Rejected records: 60" in output


def test_main_download_error(monkeypatch, capsys):
    # Simulate an API failure without using the network
    def fake_download(self):
        raise main.WeatherDownloadError("Weather API unavailable")

    monkeypatch.setattr(
        main.WeatherSource,
        "download",
        fake_download
    )

    result = main.main()
    output = capsys.readouterr().out

    assert result == 1
    assert "Weather API unavailable" in output

