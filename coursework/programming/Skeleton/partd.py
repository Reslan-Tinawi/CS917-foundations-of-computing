import csv
from typing import Optional
import sys
from exception_classes import (
    ColumnNotFoundException,
    InvalidDateTypeException,
    OutOfRangeDateException,
    InvalidDateRangeException,
)
from linear_regression import (
    calculate_line_slope,
    calculate_line_y_intercept,
)
from constants import SECONDS_PER_DAY
from helpers import filter_data_by_date_range
from exception_handling import validate_input_arguments


# Class Investment:
# Instance variables
# 	start date
# 	end date
# 	data
# Functions
# 	highest_price(data, start_date, end_date) -> float
# 	lowest_price(data, start_date, end_date) -> float
# 	max_volume(data, start_date, end_date) -> float
# 	best_avg_price(data, start_date, end_date) -> float
# 	moving_average(data, start_date, end_date) -> float
class Investment:
    def __init__(self, data: list[dict[str, str]], start_date: str, end_date: str):
        self.data = data
        self.start_date = start_date
        self.end_date = end_date

    def highest_price(
        self,
        data: Optional[list[dict[str, str]]] = None,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
    ) -> float:
        if data is None:
            data = self.data
        if start_date is None:
            start_date = self.start_date
        if end_date is None:
            end_date = self.end_date

        try:
            columns_to_check = ["time", "high"]
            validate_input_arguments(data, start_date, end_date, columns_to_check)

            filtered_data = filter_data_by_date_range(data, start_date, end_date)
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

    def lowest_price(self, data: list[dict[str, str]] = None, start_date: str = None, end_date: str = None) -> float:
        if data is None:
            data = self.data
        if start_date is None:
            start_date = self.start_date
        if end_date is None:
            end_date = self.end_date

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

    def max_volume(self, data: list[dict[str, str]] = None, start_date: str = None, end_date: str = None) -> float:
        if data is None:
            data = self.data
        if start_date is None:
            start_date = self.start_date
        if end_date is None:
            end_date = self.end_date

        try:
            columns_to_check = ["time", "volumefrom"]
            validate_input_arguments(data, start_date, end_date, columns_to_check)

            filtered_data = filter_data_by_date_range(data, start_date, end_date)
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

    def best_avg_price(self, data: list[dict[str, str]] = None, start_date: str = None, end_date: str = None) -> float:
        if data is None:
            data = self.data
        if start_date is None:
            start_date = self.start_date
        if end_date is None:
            end_date = self.end_date

        try:
            columns_to_check = ["time", "volumeto", "volumefrom"]
            validate_input_arguments(data, start_date, end_date, columns_to_check)

            filtered_data = filter_data_by_date_range(data, start_date, end_date)
            max_avg_price = max(
                map(lambda record: float(record["volumeto"]) / float(record["volumefrom"]), filtered_data)
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

    def moving_average(self, data: list[dict[str, str]] = None, start_date: str = None, end_date: str = None) -> float:
        if data is None:
            data = self.data
        if start_date is None:
            start_date = self.start_date
        if end_date is None:
            end_date = self.end_date

        try:
            columns_to_check = ["time", "volumeto", "volumefrom"]
            validate_input_arguments(data, start_date, end_date, columns_to_check)

            filtered_data = filter_data_by_date_range(data, start_date, end_date)
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


# predict_next_average(investment) -> float
# investment: Investment type
def predict_next_average(investment: Investment) -> float:
    # filter data by start_date and end_date intervals
    # start_timestamp, end_timestamp = date_to_timestamp(investment.start_date), date_to_timestamp(investment.end_date)
    # data = list(filter(lambda x: start_timestamp <= int(x.get("time")) <= end_timestamp, investment.data))
    data = filter_data_by_date_range(investment.data, investment.start_date, investment.end_date)

    # building x and y vectors
    x_list = list(map(lambda record: float(record.get("time")), data))
    y_list = list(map(lambda record: float(record["volumeto"]) / float(record["volumefrom"]), data))

    # calculating slope and y-intercept of the regression line
    line_slope = calculate_line_slope(x_list, y_list)
    line_y_intercept = calculate_line_y_intercept(x_list, y_list, line_slope)

    # getting prediction for the next day
    sample_x = x_list[-1] + SECONDS_PER_DAY
    prediction = line_slope * sample_x + line_y_intercept

    return prediction


# classify_trend(investment) -> str
# investment: Investment type
def classify_trend(investment: Investment) -> str:
    # filter data by start_date and end_date intervals
    # start_timestamp, end_timestamp = date_to_timestamp(investment.start_date), date_to_timestamp(investment.end_date)
    # data = list(filter(lambda record: start_timestamp <= int(record.get("time")) <= end_timestamp, investment.data))
    data = filter_data_by_date_range(investment.data, investment.start_date, investment.end_date)

    # building x and y vectors
    x_list = list(map(lambda record: float(record.get("time")), data))
    low_y_list = list(map(lambda record: float(record.get("low")), data))
    high_y_list = list(map(lambda record: float(record.get("high")), data))

    daily_low_slope = calculate_line_slope(x_list, low_y_list)
    daily_high_slope = calculate_line_slope(x_list, high_y_list)

    if daily_high_slope > 0 and daily_low_slope < 0:  # daily_high increasing, daily_low decreasing
        return "volatile"
    if daily_high_slope > 0 and daily_low_slope > 0:  # daily_high increasing, daily_low increasing
        return "increasing"
    if daily_high_slope < 0 and daily_low_slope < 0:  # daily_high decreasing, daily_low decreasing
        return "decreasing"
    return "other"


# Replace the body of this main function for your testing purposes
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

        for i, (start_date, end_date) in enumerate(test_data):
            investment = Investment(data, start_date, end_date)

            print("####" * 20)
            print(f"Case {i}: start_date={start_date}, end_date={end_date}")
            print(f"highest_price: {investment.highest_price()}")
            print(f"lowest_price: {investment.lowest_price()}")
            print(f"max_volume: {investment.max_volume()}")
            print(f"best_avg_price: {investment.best_avg_price()}")
            print(f"moving_average: {investment.moving_average()}")
            print("####" * 20)

        test_data = [
            ("04/05/2015", "27/05/2015"),  # 237.72045957687828 other
            ("01/02/2016", "28/02/2016"),  # 441.4238016565723 increasing
            ("08/12/2016", "11/12/2016"),  # 778.1930137752934 increasing
        ]

        for i, (start_date, end_date) in enumerate(test_data):
            investment = Investment(data, start_date, end_date)
            print("####" * 20)
            print(f"Case {i}: start_date={start_date}, end_date={end_date}")
            print(f"Next average: {predict_next_average(investment)}")
            print(f"Trend: {classify_trend(investment)}")
            print("####" * 20)

    except Exception as ex:
        ex_type = type(ex).__name__
        ex_message = ex.args
        print(f"exception type: {ex_type}")
        print(f"exception message: {ex_message}")
