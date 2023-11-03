import csv
import sys
from exception_classes import (
    ColumnNotFoundException,
    InvalidDateTypeException,
    OutOfRangeDateException,
    InvalidDateRangeException,
)
from helpers import filter_data_by_date_range, date_to_timestamp
from constants import DATA_START_DATE, DATA_END_DATE


def validate_columns(data: list[dict[str, str]], columns_to_check: list[str]) -> bool:
    """Validates that a list of columns exist in a dataset

    Args:
        data (list[dict[str, str]]): the dataset to check the columns against
        columns_to_check (list[str]): the list of columns to check existence in the dataset

    Returns:
        bool: True if _all_ columns exists in the data, False otherwise.
    """
    sample_record = data[0]
    existing_columns = set(sample_record.keys())
    columns_to_check = set(columns_to_check)
    return columns_to_check.issubset(existing_columns)


def is_in_range_date(input_date: str) -> bool:
    return DATA_START_DATE <= date_to_timestamp(input_date) <= DATA_END_DATE


def validate_input_arguments(data: list[dict[str, str]], start_date: str, end_date: str, columns_to_check: list[str]):
    """_summary_

    Args:
        data (list[dict[str, str]]): _description_
        start_date (str): _description_
        end_date (str): _description_
        columns_to_check (list[str]): _description_

    Raises:
        ColumnNotFoundException: _description_
        InvalidDateTypeException: _description_
        OutOfRangeDateException: _description_
        InvalidDateRangeException: _description_
    """
    if not validate_columns(data, columns_to_check):
        raise ColumnNotFoundException("Error: requested column is missing from datase")

    if isinstance(start_date, int) or isinstance(end_date, int):
        raise InvalidDateTypeException("Error: invalid date value")

    if not (is_in_range_date(start_date) and is_in_range_date(end_date)):
        raise OutOfRangeDateException(f"Error: date value is out of range")

    start_timestamp, end_timestamp = date_to_timestamp(start_date), date_to_timestamp(end_date)

    if end_timestamp > start_timestamp:
        raise InvalidDateRangeException("Error: end date must be larger than start date")


# highest_price(data, start_date, end_date) -> float
# data: the data from a csv file
# start_date: string in "dd/mm/yyyy" format
# start_date: string in "dd/mm/yyyy" format
def highest_price(data: list[dict[str, str]], start_date: str, end_date: str) -> float:
    try:
        columns_to_check = ["time", "high"]
        validate_input_arguments(data, start_date, end_date, columns_to_check)

        filtered_data = filter_data_by_date_range(data, start_date, end_date, "time")
        highest_value = max(map(lambda record: float(record.get("high")), filtered_data))
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

        filtered_data = filter_data_by_date_range(data, start_date, end_date, "time")
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

        filtered_data = filter_data_by_date_range(data, start_date, end_date, "time")
        max_exchanged_volume = max(map(lambda record: float(record.get("volumefrom")), filtered_data))
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

        filtered_data = filter_data_by_date_range(data, start_date, end_date, "time")
        max_avg_price = max(map(lambda record: float(record["volumeto"]) / float(record["volumefrom"]), filtered_data))
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

        filtered_data = filter_data_by_date_range(data, start_date, end_date, "time")
        daily_averages = list(
            map(lambda record: float(record["volumeto"]) / float(record["volumefrom"]), filtered_data)
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


# Replace the body of this main function for your testing purposes
if __name__ == "__main__":
    # Start the program

    # Example variable initialization
    # data is always the cryptocompare_btc.csv read in using a DictReader

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
