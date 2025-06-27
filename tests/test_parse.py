from app.utils.parse import get_avg_data


def test_get_avg_data():
    avg_data = get_avg_data()
    assert all(isinstance(value, float) for value in avg_data.values())
