import csv
from typing import Optional
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
from helpers import filter_data_by_date_range, date_to_timestamp


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
        # self.data = data
        # TODO:
        #   is this appropriate here?
        #   adding `volume_ratio` attributes
        #   Also, why not convert `time` to integer here? NOOOOO
        self.data = [
            dict(record, volume_ratio=float(record["volumeto"]) / float(record["volumefrom"])) for record in data
        ]
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

        filtered_data = filter_data_by_date_range(data, start_date, end_date)
        highest_value_dict = max(filtered_data, key=lambda record: float(record["high"]))
        highest_value = float(highest_value_dict.get("high"))
        return highest_value

    def lowest_price(self, data: list[dict[str, str]] = None, start_date: str = None, end_date: str = None) -> float:
        if data is None:
            data = self.data
        if start_date is None:
            start_date = self.start_date
        if end_date is None:
            end_date = self.end_date

        filtered_data = filter_data_by_date_range(data, start_date, end_date)
        lowset_value_dict = min(filtered_data, key=lambda record: float(record["low"]))
        lowset_value = float(lowset_value_dict.get("low"))
        return float(lowset_value)

    def max_volume(self, data: list[dict[str, str]] = None, start_date: str = None, end_date: str = None) -> float:
        if data is None:
            data = self.data
        if start_date is None:
            start_date = self.start_date
        if end_date is None:
            end_date = self.end_date

        filtered_data = filter_data_by_date_range(data, start_date, end_date)
        max_exchanged_volume_dict = max(filtered_data, key=lambda record: float(record["volumefrom"]))
        max_exchanged_volume = float(max_exchanged_volume_dict.get("volumefrom"))
        return float(max_exchanged_volume)

    def best_avg_price(self, data: list[dict[str, str]] = None, start_date: str = None, end_date: str = None) -> float:
        if data is None:
            data = self.data
        if start_date is None:
            start_date = self.start_date
        if end_date is None:
            end_date = self.end_date

        filtered_data = filter_data_by_date_range(data, start_date, end_date)
        max_avg_price_dict = max(
            filtered_data, key=lambda record: float(record["volumeto"]) / float(record["volumefrom"])
        )

        max_volume_to = float(max_avg_price_dict.get("volumeto"))
        max_volume_from = float(max_avg_price_dict.get("volumefrom"))
        max_avg_price = max_volume_to / max_volume_from

        return float(max_avg_price)

    def moving_average(self, data: list[dict[str, str]] = None, start_date: str = None, end_date: str = None) -> float:
        if data is None:
            data = self.data
        if start_date is None:
            start_date = self.start_date
        if end_date is None:
            end_date = self.end_date

        filtered_data = filter_data_by_date_range(data, start_date, end_date)
        daily_averages = list(
            map(lambda record: float(record["volumeto"]) / float(record["volumefrom"]), filtered_data)
        )
        moving_avg = sum(daily_averages) * 1.0 / len(daily_averages)
        return round(moving_avg, 2)


# predict_next_average(investment) -> float
# investment: Investment type
def predict_next_average(investment: Investment) -> float:
    # filter data by start_date and end_date intervals
    # TODO:
    #   convert start_date and end_date from date to timestamp
    start_timestamp, end_timestamp = date_to_timestamp(investment.start_date), date_to_timestamp(investment.end_date)
    data = list(filter(lambda x: start_timestamp <= int(x.get("time")) <= end_timestamp, investment.data))

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
    # TODO:
    #   convert start_date and end_date from date to timestamp
    start_timestamp, end_timestamp = date_to_timestamp(investment.start_date), date_to_timestamp(investment.end_date)
    data = list(filter(lambda x: start_timestamp <= int(x.get("time")) <= end_timestamp, investment.data))

    # building x and y vectors
    x_list = list(map(lambda record: float(record.get("time")), data))
    low_y_list = list(map(lambda record: record.get("high"), data))
    high_y_list = list(map(lambda record: record.get("low"), data))

    daily_low_slope = calculate_line_slope(x_list, low_y_list)
    daily_high_slope = calculate_line_slope(x_list, high_y_list)

    if daily_high_slope > 0 & daily_low_slope < 0:  # daily_high increasing, daily_low decreasing
        return "volatile"
    if daily_high_slope > 0 & daily_low_slope > 0:  # daily_high increasing, daily_low increasing
        return "increasing"
    if daily_high_slope < 0 & daily_low_slope < 0:  # daily_high decreasing, daily_low decreasing
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

    except Exception as ex:
        ex_type = type(ex).__name__
        ex_message = ex.args
        print(f"exception type: {ex_type}")
        print(f"exception message: {ex_message}")
