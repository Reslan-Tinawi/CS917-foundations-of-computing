import csv

"""
    Part B
    Please provide definitions for the following functions *WITH EXCEPTION HANDLERS*
"""

# highest_price(data, start_date, end_date) -> float
# data: the data from a csv file
# start_date: string in "dd/mm/yyyy" format
# start_date: string in "dd/mm/yyyy" format
def  highest_price(data, start_date, end_date):
	 
	 #replace None with an appropriate return value
	 return None


# lowest_price(data, start_date, end_date) -> float
# data: the data from a csv file
# start_date: string in "dd/mm/yyyy" format
# start_date: string in "dd/mm/yyyy" format
def  lowest_price(data, start_date, end_date):
	 
	 #replace None with an appropriate return value
	 return None



# max_volume(data, start_date, end_date) -> float
# data: the data from a csv file
# start_date: string in "dd/mm/yyyy" format
# start_date: string in "dd/mm/yyyy" format
def  max_volume(data, start_date, end_date):
	 
	 #replace None with an appropriate return value
	 return None



# best_avg_price(data, start_date, end_date) -> float
# data: the data from a csv file
# start_date: string in "dd/mm/yyyy" format
# start_date: string in "dd/mm/yyyy" format
def  best_avg_price(data, start_date, end_date):
	 
	 #replace None with an appropriate return value
	 return None




# moving_average(data, start_date, end_date) -> float
# data: the data from a csv file
# start_date: string in "dd/mm/yyyy" format
# start_date: string in "dd/mm/yyyy" format
def  moving_average(data, start_date, end_date):
	 
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
