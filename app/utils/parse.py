import csv


def get_avg_data() -> dict[str, float]:
    state_count = dict()
    state_price = dict()
    with open("data/coding_challenge_prices.csv", "r", encoding="utf-8") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            state_id = row["state"].upper()
            state_count[state_id] = state_count.get(state_id, 0) + 1
            state_price[state_id] = round(state_price.get(state_id, 0) + float(row["price"]), 2)
    return { key: round(state_price[key] / state_count[key], 2) for key in state_count.keys() }
