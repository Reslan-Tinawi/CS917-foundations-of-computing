from constants import DATA_START_TIMESTAMP, DATA_END_TIMESTAMP
from helpers import date_to_timestamp
from exception_classes import (
    ColumnNotFoundException,
    InvalidDateTypeException,
    OutOfRangeDateException,
    InvalidDateRangeException,
)


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
    return DATA_START_TIMESTAMP <= date_to_timestamp(input_date) <= DATA_END_TIMESTAMP


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
        raise ColumnNotFoundException("Error: requested column is missing from dataset")

    if isinstance(start_date, int) or isinstance(end_date, int):
        raise InvalidDateTypeException("Error: invalid date value")

    if not (is_in_range_date(start_date) and is_in_range_date(end_date)):
        raise OutOfRangeDateException(f"Error: date value is out of range")

    start_timestamp, end_timestamp = date_to_timestamp(start_date), date_to_timestamp(end_date)

    if end_timestamp < start_timestamp:
        raise InvalidDateRangeException("Error: end date must be larger than start date")
