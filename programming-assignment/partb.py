import csv
import sys
from exception_classes import (
    ColumnNotFoundException,
    InvalidDateTypeException,
    OutOfRangeDateException,
    InvalidDateRangeException,
)
from helpers import filter_data_by_date_range
from exception_handling import validate_input_arguments


# highest_price(data, start_date, end_date) -> float
# data: the data from a csv file
# start_date: string in "dd/mm/yyyy" format
# start_date: string in "dd/mm/yyyy" format
def highest_price(data: list[dict[str, str]], start_date: str, end_date: str) -> float:
    try:
        columns_to_check = ["time", "high"]
        validate_input_arguments(data, start_date, end_date, columns_to_check)

        filtered_data = filter_data_by_date_range(data, start_date, end_date)
        highest_value = max(
            map(lambda record: float(record.get("high")), filtered_data)
        )
        return highest_value
    except (
        ColumnNotFoundException,
        InvalidDateTypeException,
        OutOfRangeDateException,
        InvalidDateRangeException,
    ) as ex:
        print(ex.args)
        sys.exit()


# lowest_price(data, start_date, end_date) -> float
# data: the data from a csv file
# start_date: string in "dd/mm/yyyy" format
# start_date: string in "dd/mm/yyyy" format
def lowest_price(data, start_date, end_date):
    try:
        columns_to_check = ["time", "low"]
        validate_input_arguments(data, start_date, end_date, columns_to_check)

        filtered_data = filter_data_by_date_range(data, start_date, end_date)
        lowset_value = min(map(lambda record: float(record.get("low")), filtered_data))
        return lowset_value
    except (
        ColumnNotFoundException,
        InvalidDateTypeException,
        OutOfRangeDateException,
        InvalidDateRangeException,
    ) as ex:
        print(ex.args)
        sys.exit()


# max_volume(data, start_date, end_date) -> float
# data: the data from a csv file
# start_date: string in "dd/mm/yyyy" format
# start_date: string in "dd/mm/yyyy" format
def max_volume(data, start_date, end_date):
    try:
        columns_to_check = ["time", "volumefrom"]
        validate_input_arguments(data, start_date, end_date, columns_to_check)

        filtered_data = filter_data_by_date_range(data, start_date, end_date)
        max_exchanged_volume = max(
            map(lambda record: float(record.get("volumefrom")), filtered_data)
        )
        return max_exchanged_volume
    except (
        ColumnNotFoundException,
        InvalidDateTypeException,
        OutOfRangeDateException,
        InvalidDateRangeException,
    ) as ex:
        print(ex.args)
        sys.exit()


# best_avg_price(data, start_date, end_date) -> float
# data: the data from a csv file
# start_date: string in "dd/mm/yyyy" format
# start_date: string in "dd/mm/yyyy" format
def best_avg_price(data, start_date, end_date):
    try:
        columns_to_check = ["time", "volumeto", "volumefrom"]
        validate_input_arguments(data, start_date, end_date, columns_to_check)

        filtered_data = filter_data_by_date_range(data, start_date, end_date)
        max_avg_price = max(
            map(
                lambda record: float(record["volumeto"]) / float(record["volumefrom"]),
                filtered_data,
            )
        )
        return max_avg_price
    except (
        ColumnNotFoundException,
        InvalidDateTypeException,
        OutOfRangeDateException,
        InvalidDateRangeException,
    ) as ex:
        print(ex.args)
        sys.exit()


# moving_average(data, start_date, end_date) -> float
# data: the data from a csv file
# start_date: string in "dd/mm/yyyy" format
# start_date: string in "dd/mm/yyyy" format
def moving_average(data, start_date, end_date):
    try:
        columns_to_check = ["time", "volumeto", "volumefrom"]
        validate_input_arguments(data, start_date, end_date, columns_to_check)

        filtered_data = filter_data_by_date_range(data, start_date, end_date)
        daily_averages = list(
            map(
                lambda record: float(record["volumeto"]) / float(record["volumefrom"]),
                filtered_data,
            )
        )
        moving_avg = sum(daily_averages) * 1.0 / len(daily_averages)
        return round(moving_avg, 2)
    except (
        ColumnNotFoundException,
        InvalidDateTypeException,
        OutOfRangeDateException,
        InvalidDateRangeException,
    ) as ex:
        print(ex.args)
        sys.exit()


if __name__ == "__main__":
    data = []
    dataset_file_path = "cryptocompare_btc.csv"

    try:
        with open(dataset_file_path, "r") as f:
            reader = csv.DictReader(f)
            data = [r for r in reader]

        test_data = [
            ("01/01/2016", "31/01/2016"),
            ("01/02/2016", "28/02/2016"),
            ("01/12/2016", "31/12/2016"),
        ]

        for i, sample_test in enumerate(test_data):
            start_date, end_date = sample_test

            print("####" * 20)
            print(f"Case {i}: start_date={start_date}, end_date={end_date}")
            print(f"highest_price: {highest_price(data, start_date, end_date)}")
            print(f"lowest_price: {lowest_price(data, start_date, end_date)}")
            print(f"max_volume: {max_volume(data, start_date, end_date)}")
            print(f"best_avg_price: {best_avg_price(data, start_date, end_date)}")
            print(f"moving_average: {moving_average(data, start_date, end_date)}")
            print("####" * 20)

    except FileNotFoundError:
        print("Error: dataset not found")
        sys.exit()
