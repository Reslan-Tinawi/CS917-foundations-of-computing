import csv
import calendar
import time
from typing import Any

"""
    Part A
    Please provide definitions for the following functions
"""


def date_to_timestamp(input_date: str) -> int:
    return calendar.timegm(time.strptime(input_date, "%d/%m/%Y"))


def filter_data_by_date_range(
    data: list[dict[str | Any, str | Any]], start_date: str, end_date: str
) -> list[dict[str | Any, str | Any]]:
    start_timestamp, end_timestamp = date_to_timestamp(start_date), date_to_timestamp(end_date)

    filtered_data = list(filter(lambda record: start_timestamp <= int(record["time"]) <= end_timestamp, data))

    return filtered_data


# highest_price(data, start_date, end_date) -> float
# data: the data from a csv file
# start_date: string in "dd/mm/yyyy" format
# start_date: string in "dd/mm/yyyy" format
def highest_price(data: list[dict[str | Any, str | Any]], start_date: str, end_date: str) -> float:
    filtered_data = filter_data_by_date_range(data, start_date, end_date)
    highest_value_dict = max(filtered_data, key=lambda record: float(record["high"]))
    highest_value = float(highest_value_dict.get("high"))
    return highest_value


# lowest_price(data, start_date, end_date) -> float
# data: the data from a csv file
# start_date: string in "dd/mm/yyyy" format
# start_date: string in "dd/mm/yyyy" format
def lowest_price(data: list[dict[str | Any, str | Any]], start_date: str, end_date: str) -> float:
    filtered_data = filter_data_by_date_range(data, start_date, end_date)
    lowset_value_dict = min(filtered_data, key=lambda record: float(record["low"]))
    lowset_value = float(lowset_value_dict.get("low"))
    return float(lowset_value)


# max_volume(data, start_date, end_date) -> float
# data: the data from a csv file
# start_date: string in "dd/mm/yyyy" format
# start_date: string in "dd/mm/yyyy" format
def max_volume(data, start_date, end_date):
    filtered_data = filter_data_by_date_range(data, start_date, end_date)
    max_exchanged_volume_dict = max(filtered_data, key=lambda record: float(record["volumefrom"]))
    max_exchanged_volume = float(max_exchanged_volume_dict.get("volumefrom"))
    return float(max_exchanged_volume)


# best_avg_price(data, start_date, end_date) -> float
# data: the data from a csv file
# start_date: string in "dd/mm/yyyy" format
# start_date: string in "dd/mm/yyyy" format
def best_avg_price(data, start_date, end_date) -> float:
    filtered_data = filter_data_by_date_range(data, start_date, end_date)
    max_avg_price_dict = max(filtered_data, key=lambda record: float(record["volumeto"]) / float(record["volumefrom"]))

    max_volume_to = float(max_avg_price_dict.get("volumeto"))
    max_volume_from = float(max_avg_price_dict.get("volumefrom"))
    max_avg_price = max_volume_to / max_volume_from

    return float(max_avg_price)


# moving_average(data, start_date, end_date) -> float
# data: the data from a csv file
# start_date: string in "dd/mm/yyyy" format
# start_date: string in "dd/mm/yyyy" format
def moving_average(data, start_date, end_date) -> float:
    filtered_data = filter_data_by_date_range(data, start_date, end_date)
    daily_averages = list(map(lambda record: float(record["volumeto"]) / float(record["volumefrom"]), filtered_data))
    moving_avg = sum(daily_averages) * 1.0 / len(daily_averages)
    return round(moving_avg, 2)


# Replace the body of this main function for your testing purposes
if __name__ == "__main__":
    # Start the program

    # Example variable initialization
    # data is always the cryptocompare_btc.csv read in using a DictReader

    data = []
    with open("cryptocompare_btc.csv", "r") as f:
        reader = csv.DictReader(f)
        data = [r for r in reader]

    # access individual rows from data using list indices
    first_row = data[0]
    # to access row values, use relevant column heading in csv
    print(f"timestamp = {first_row['time']}")
    print(f"daily high = {first_row['high']}")
    print(f"volume in BTC = {first_row['volumefrom']}")

    pass
