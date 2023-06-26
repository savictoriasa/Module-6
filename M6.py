'''
#CURRENT TIME FUNCTIONING CODE
from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)

#PROFESSOR'S CODE
import sys
from datetime import datetime
from datetime import time
from datetime import date

def main():
     dt = datetime.now()
     time_string = dt.strftime("%X")
     print(time_string)
     for line in sys.stdin:
          data = line.strip().split("\t")
     if len(data) == 6:
          _date, _time, store, item, cost, payment = data
print("{dt}\t{time_string}\t{store}\t{item}\t{cost}\t{payment}")

main()

#EXERCISE #3 WORKING
from datetime import timedelta

d = timedelta(microseconds=-1)
(d.days, d.seconds, d.microseconds)
(-1, 86399, 999999)

d = timedelta(days = 100, hours = 10, minutes = 13)
print(d)
'''






from datetime import datetime 
# get current date
def function(feet, inches):
     feet = 1
     inches = 12
     datetime_object = datetime.now()
     print(datetime_object)
     print('Type :- ', (datetime_object))
     function(feet,inches)

