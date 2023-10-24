import csv

"""
    Part C
    Please provide definitions for the following functions
"""

# moving_avg_short(data, start_date, end_date) -> dict
# data: the data from a csv file
# start_date: string in "dd/mm/yyyy" format
# start_date: string in "dd/mm/yyyy" format
def  moving_avg_short(data, start_date, end_date):
	 
	 #replace None with an appropriate return value
	 return None


# moving_avg_long(data, start_date, end_date) -> dict
# data: the data from a csv file
# start_date: string in "dd/mm/yyyy" format
# start_date: string in "dd/mm/yyyy" format
def  moving_avg_long(data, start_date, end_date):
	 
	 #replace None with an appropriate return value
	 return None



# find_buy_list(short_avg_dict, long_avg_dict) -> dict
# data: the data from a csv file
# start_date: string in "dd/mm/yyyy" format
# start_date: string in "dd/mm/yyyy" format
def  find_buy_list(short_avg_dict, long_avg_dict):
	 
	 #replace None with an appropriate return value
	 return None



# find_sell_list(short_avg_dict, long_avg_dict) -> dict
# data: the data from a csv file
# start_date: string in "dd/mm/yyyy" format
# start_date: string in "dd/mm/yyyy" format
def  find_sell_list(short_avg_dict, long_avg_dict):
	 
	 #replace None with an appropriate return value
	 return None



# crossover_method(data, start_date, end_date) -> [buy_list, sell_list]
# data: the data from a csv file
# start_date: string in "dd/mm/yyyy" format
# start_date: string in "dd/mm/yyyy" format
def  crossover_method(data, start_date, end_date):
	 
	 #replace None with an appropriate return value
	 return None


# Replace the body of this main function for your testing purposes
if __name__ == "__main__":
    # Start the program

    # Example variable initialization
    # data is always the cryptocompare_btc.csv read in using a DictReader
    
    data = []
    with open("cryptocompare_btc.csv", "r") as f:
        reader = csv.DictReader(f)
        data = [r for r in reader]
    
    pass

