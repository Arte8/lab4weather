
import json


def test_write_temporary_json(tmp_path):
    # Create a temporary JSON file
    output_file = tmp_path / "weather_summary.json"

    sample_data = {
        "temperature": 18.5,
        "precipitation": 0.2
    }

    # Write sample data
    output_file.write_text(
        json.dumps(sample_data),
        encoding="utf-8"
    )

    # Read it back
    saved_data = json.loads(
        output_file.read_text(encoding="utf-8")
    )

    assert output_file.exists()
    assert saved_data["temperature"] == 18.5
    assert saved_data["precipitation"] == 0.2
