import calendar
import time

# data start date and end date
DATA_START_DATE = "28/04/2015"
DATA_END_DATE = "18/10/2020"

DATA_START_TIMESTAMP = calendar.timegm(time.strptime(DATA_START_DATE, "%d/%m/%Y"))
DATA_END_TIMESTAMP = calendar.timegm(time.strptime(DATA_END_DATE, "%d/%m/%Y"))

# moving average window sizes
SHORT_WINDOW_SIZE = 3
LONG_WINDOW_SIZE = 10

# total seconds per day: 24 hours * 60 minutes * 60 seconds
SECONDS_PER_DAY = 24 * 60 * 60
