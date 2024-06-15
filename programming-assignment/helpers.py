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


def timestamp_to_date(input_timestamp: int, format: str = "%d/%m/%Y") -> str:
    """This utility function converts UNIX timestamp to a date string using the default format "dd/mm/yyyy"

    Args:
        input_timestamp (int): a timestampt to convert to date
        format (str, optional): date format. Defaults to "%d/%m/%Y".

    Returns:
        str: a date string formatted as specified in format argument
    """
    return time.strftime(format, time.gmtime(input_timestamp))


def filter_data_by_date_range(
    data: list[dict[str, str]],
    start_date: str,
    end_date: str,
) -> list[dict[str, str]]:
    """This function filters the dataset to return only records
    that lies within a date range.

    Args:
        data (list[dict[str, str]]): The dataset. A list of dictionaries where each dictionary represents a row in the csv file
        start_date (str): start date of the filtering interval in "dd/mm/yyyy" format
        end_date (str): end date of the filtering interval in "dd/mm/yyyy" format

    Returns:
        list[dict[str, str]]: filtered dataset that includes only records which fall in the filtering date interval
    """
    # convert from string format to timestamp
    start_timestamp, end_timestamp = date_to_timestamp(start_date), date_to_timestamp(
        end_date
    )

    filtered_data = list(
        filter(
            lambda record: start_timestamp <= int(record["time"]) <= end_timestamp, data
        )
    )

    return filtered_data


def get_record_index(data: dict[str, str], date_value) -> int:
    """Returns the index of a record based on its date value

    Args:
        data (dict[str, str]): the dataset (list of dictionaries)
        date_value (_type_): the date value to get index for

    Returns:
        int: element index between 0 and len(data). -1 if element not found
    """
    element_position = [
        index
        for index, record in enumerate(data)
        if int(record.get("time")) == date_value
    ]
    if len(element_position) == 0:
        return -1
    return element_position[0]


def calculate_window_moving_average(
    data: list[dict[str, str]], dt: int, window_size: int
) -> float:
    """This function calculates the price moving average for a given window size.

    Args:
        data (list[dict[str, str]]): the dataset (list of records)
        dt (int): the date value at which to calculate the moving average
        window_size (int): the window size.

    Returns:
        float: the moving average at the specified date
    """
    # calculate window start and end indices
    # take into account cases when the date is very close to the start of the start of the dataset
    end_idx = get_record_index(data, dt) + 1
    start_idx = max(0, end_idx - window_size)

    # extract list of the daily average prices (volumeto / volumefrom) for the corresponding dates
    daily_avg_price_list = list(
        map(
            lambda record: float(record["volumeto"]) / float(record["volumefrom"]),
            data[start_idx:end_idx],
        )
    )

    # return the window average
    return sum(daily_avg_price_list) * 1.0 / len(daily_avg_price_list)
