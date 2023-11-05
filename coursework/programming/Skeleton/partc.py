import csv
from helpers import filter_data_by_date_range, timestamp_to_date, calculate_window_moving_average
from constants import SHORT_WINDOW_SIZE, LONG_WINDOW_SIZE


# moving_avg_short(data, start_date, end_date) -> dict
# data: the data from a csv file
# start_date: string in "dd/mm/yyyy" format
# start_date: string in "dd/mm/yyyy" format
def moving_avg_short(data: list[dict[str, str]], start_date: str, end_date: str) -> dict[str, float]:
    # List of dates between `start_date` and `end_date`
    dates_list = list(
        map(lambda record: int(record.get("time")), filter_data_by_date_range(data, start_date, end_date))
    )

    # store the moving average value for each date
    short_moving_avg_dict = {
        timestamp_to_date(dt): calculate_window_moving_average(data, dt, SHORT_WINDOW_SIZE) for dt in dates_list
    }

    return short_moving_avg_dict


# moving_avg_long(data, start_date, end_date) -> dict
# data: the data from a csv file
# start_date: string in "dd/mm/yyyy" format
# start_date: string in "dd/mm/yyyy" format
def moving_avg_long(data: list[dict[str, str]], start_date: str, end_date: str) -> dict[str, float]:
    # List of dates betwenn `start_date` and `end_date`
    dates_list = list(
        map(lambda record: int(record.get("time")), filter_data_by_date_range(data, start_date, end_date))
    )

    # store the moving average value for each date
    long_moving_avg_dict = {
        timestamp_to_date(dt): calculate_window_moving_average(data, dt, LONG_WINDOW_SIZE) for dt in dates_list
    }

    return long_moving_avg_dict


# find_buy_list(short_avg_dict, long_avg_dict) -> dict
# data: the data from a csv file
# start_date: string in "dd/mm/yyyy" format
# start_date: string in "dd/mm/yyyy" format
def find_buy_list(short_avg_dict: dict[str, float], long_avg_dict: dict[str, float]) -> dict[str, int]:
    dates_list = list(short_avg_dict.keys())
    # initialize the dictionary with "0" for all days
    result = {dt: 0 for dt in dates_list}

    first_day = dates_list[0]

    # previous_diff: difference between the averages at day t-1
    # current_diff: difference between the averages at day t
    previous_diff = short_avg_dict.get(first_day) - long_avg_dict.get(first_day)
    current_diff = 0

    for dt in dates_list[1:]:
        current_diff = short_avg_dict.get(dt) - long_avg_dict.get(dt)

        # if short_avg is larger than long_avg at day t, and it was smaller or equal at day t - 1
        # then this is a *buying* (crossing upward)  day
        if previous_diff <= 0 and current_diff > 0:
            result[dt] = 1

        previous_diff = current_diff

    return result


# find_sell_list(short_avg_dict, long_avg_dict) -> dict
# data: the data from a csv file
# start_date: string in "dd/mm/yyyy" format
# start_date: string in "dd/mm/yyyy" format
def find_sell_list(short_avg_dict: dict[str, float], long_avg_dict: dict[str, float]) -> dict[str, int]:
    dates_list = list(short_avg_dict.keys())
    # initialize the dictionary with "0" for all days
    result = {dt: 0 for dt in dates_list}

    first_day = dates_list[0]

    # previous_diff: difference between the averages at day t-1
    # current_diff: difference between the averages at day t
    previous_diff = short_avg_dict.get(first_day) - long_avg_dict.get(first_day)
    current_diff = 0

    for dt in dates_list[1:]:
        current_diff = short_avg_dict.get(dt) - long_avg_dict.get(dt)

        # if short_avg is smaller than long_avg at day t, and it was larger or equal at day t - 1
        # then this is a *selling* (crossing downward) day
        if previous_diff >= 0 and current_diff < 0:
            result[dt] = 1

        previous_diff = current_diff

    return result


# crossover_method(data, start_date, end_date) -> [buy_list, sell_list]
# data: the data from a csv file
# start_date: string in "dd/mm/yyyy" format
# start_date: string in "dd/mm/yyyy" format
def crossover_method(data, start_date, end_date) -> list[list[str], list[str]]:
    short_moving_avg_dict = moving_avg_short(data, start_date, end_date)
    long_moving_avg_dict = moving_avg_long(data, start_date, end_date)

    buy_dict = find_buy_list(short_moving_avg_dict, long_moving_avg_dict)
    sell_dict = find_sell_list(short_moving_avg_dict, long_moving_avg_dict)

    buy_list = [k for k, v in buy_dict.items() if v]
    sell_list = [k for k, v in sell_dict.items() if v]

    return [buy_list, sell_list]


if __name__ == "__main__":
    data = []
    with open("cryptocompare_btc.csv", "r") as f:
        reader = csv.DictReader(f)
        data = [r for r in reader]

    test_data = [
        ("01/05/2017", "12/06/2017"),
        ("05/09/2018", "27/09/2018"),
        ("03/11/2019", "14/11/2019"),
        ("28/04/2015", "28/05/2015"),
    ]

    for i, (start_date, end_date) in enumerate(test_data):
        print("####" * 20)
        print(f"Case {i}: start_date={start_date}, end_date={end_date}")
        print(crossover_method(data, start_date, end_date))
        print("####" * 20)
