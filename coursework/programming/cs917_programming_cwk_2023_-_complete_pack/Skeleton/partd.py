import matplotlib.pyplot as plt
import csv

"""
    Part D
    Please provide definitions for the following class and functions
"""

# Class Investment:
# Instance variables
#	start date
#	end date
#	data 
#Functions
#	highest_price(data, start_date, end_date) -> float
#	lowest_price(data, start_date, end_date) -> float
#	max_volume(data, start_date, end_date) -> float
#	best_avg_price(data, start_date, end_date) -> float
#	moving_average(data, start_date, end_date) -> float
class Investment:
    pass




# predict_next_average(investment) -> float
# investment: Investment type
def	predict_next_average(investment):
		
	#replace None with an appropriate return value
	return None


# classify_trend(investment) -> str
# investment: Investment type
def classify_trend(investment):

	#replace None with an appropriate return value
	return None
	
	



# Replace the body of this main function for your testing purposes
if __name__ == "__main__":
    # Start the program
    data = []
    with open("ftse100.csv", "r") as f:
        reader = csv.DictReader(f)
        data = [r for r in reader]
    pass
