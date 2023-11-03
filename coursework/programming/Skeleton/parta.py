import csv
from helpers import filter_data_by_date_range


# highest_price(data, start_date, end_date) -> float
# data: the data from a csv file
# start_date: string in "dd/mm/yyyy" format
# start_date: string in "dd/mm/yyyy" format
def highest_price(data: list[dict[str, str]], start_date: str, end_date: str) -> float:
    filtered_data = filter_data_by_date_range(data, start_date, end_date, "time")
    highest_value = max(map(lambda record: float(record.get("high")), filtered_data))
    return highest_value


# lowest_price(data, start_date, end_date) -> float
# data: the data from a csv file
# start_date: string in "dd/mm/yyyy" format
# start_date: string in "dd/mm/yyyy" format
def lowest_price(data: list[dict[str, str]], start_date: str, end_date: str) -> float:
    filtered_data = filter_data_by_date_range(data, start_date, end_date, "time")
    lowest_value = min(map(lambda record: float(record.get("low")), filtered_data))
    return lowest_value


# max_volume(data, start_date, end_date) -> float
# data: the data from a csv file
# start_date: string in "dd/mm/yyyy" format
# start_date: string in "dd/mm/yyyy" format
def max_volume(data, start_date, end_date):
    filtered_data = filter_data_by_date_range(data, start_date, end_date, "time")
    max_exchanged_volume = max(map(lambda record: float(record.get("volumefrom")), filtered_data))
    return max_exchanged_volume


# best_avg_price(data, start_date, end_date) -> float
# data: the data from a csv file
# start_date: string in "dd/mm/yyyy" format
# start_date: string in "dd/mm/yyyy" format
def best_avg_price(data, start_date, end_date) -> float:
    filtered_data = filter_data_by_date_range(data, start_date, end_date, "time")
    max_avg_price = max(map(lambda record: float(record["volumeto"]) / float(record["volumefrom"]), filtered_data))
    return max_avg_price


# moving_average(data, start_date, end_date) -> float
# data: the data from a csv file
# start_date: string in "dd/mm/yyyy" format
# start_date: string in "dd/mm/yyyy" format
def moving_average(data, start_date, end_date) -> float:
    filtered_data = filter_data_by_date_range(data, start_date, end_date, "time")
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
