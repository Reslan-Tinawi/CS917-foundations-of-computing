import calendar
import time


def date_to_timestamp(input_date: str) -> int:
    """This utility function converts date from string format "dd/mm/yyyy" to UNIX timestamp

    Args:
        input_date (str): the input date string in format "dd/mm/yyyy" that we want to convert to timestamp

    Returns:
        int: the corresponding timestamp value of the passed string date value
    """
    return calendar.timegm(time.strptime(input_date, "%d/%m/%Y"))


def filter_data_by_date_range(
    data: list[dict[str, str]], start_date: str, end_date: str, attribute_name: str
) -> list[dict[str, str]]:
    """This function filters the dataset to return only records
    that lies within a date range.

    Args:
        data (list[dict[str, str]]): The dataset. A list of dictionaries where each dictionary represents a row in the csv file
        start_date (str): start date of the filtering interval in "dd/mm/yyyy" format
        end_date (str): end date of the filtering interval in "dd/mm/yyyy" format
        attribute_name (str): name of the date attribute in the dataset to use for filtering

    Returns:
        list[dict[str, str]]: filtered dataset that includes only records which fall in the filtering date interval
    """
    # convert from string format to timestamp
    start_timestamp, end_timestamp = date_to_timestamp(start_date), date_to_timestamp(end_date)

    filtered_data = list(filter(lambda record: start_timestamp <= int(record[attribute_name]) <= end_timestamp, data))

    return filtered_data
