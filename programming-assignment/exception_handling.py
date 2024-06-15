"""
    Function for validating function arguments
"""

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
    """Validates that input date is within the data date range

    Args:
        input_date (str): input date to validate

    Returns:
        bool: True if the input date is within the data start and end dates. False otherwise
    """
    return DATA_START_TIMESTAMP <= date_to_timestamp(input_date) <= DATA_END_TIMESTAMP


def validate_input_arguments(
    data: list[dict[str, str]],
    start_date: str,
    end_date: str,
    columns_to_check: list[str],
):
    """This function validates the input arguments

    Args:
        data (list[dict[str, str]]): the dataset (list of records)
        start_date (str): start date string
        end_date (str): end date string
        columns_to_check (list[str]): list of columns to check existence in the dataset

    Raises:
        ColumnNotFoundException: if one of the columns in `columns_to_check` doesn't exist in the dataset
        InvalidDateTypeException: if `start_date` or `end_date` are not of string type
        OutOfRangeDateException: if `start_date` is small than the data "28/04/2015" or `end_date` is larger than "18/10/2020"
        InvalidDateRangeException: if `end_date` is smaller than `start_date`
    """
    if not validate_columns(data, columns_to_check):
        raise ColumnNotFoundException("Error: requested column is missing from dataset")

    if isinstance(start_date, int) or isinstance(end_date, int):
        raise InvalidDateTypeException("Error: invalid date value")

    if not (is_in_range_date(start_date) and is_in_range_date(end_date)):
        raise OutOfRangeDateException(f"Error: date value is out of range")

    start_timestamp, end_timestamp = date_to_timestamp(start_date), date_to_timestamp(
        end_date
    )

    if end_timestamp < start_timestamp:
        raise InvalidDateRangeException(
            "Error: end date must be larger than start date"
        )
