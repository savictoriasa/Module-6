#EXERCISE 1
#CURRENT TIME CODE THAT I UNDERSTOOD
from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)


#TRYING TO MAKE PROFESSOR'S CODE WORK
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


#EXERCISE 2
from datetime import datetime, timedelta

finalt = (datetime.now() - timedelta(seconds = 60)).strftime('%Y:%H:%M:%S')
print("Time minus 60 seconds: " + finalt)

finaly = (datetime.now() + timedelta(hours = 17520)).strftime('%Y:%H:%M:%S')
print("Time plus 2 years: " + finaly)

endtime = (datetime.now() + timedelta(hours = 17520) - timedelta(seconds = 60)).strftime('%Y:%H:%M:%S')
print("Final time minus 60 seconds and plus 2 years: " + endtime)


#EXERCISE 3 
from datetime import timedelta

d = timedelta(microseconds=-1)
(d.days, d.seconds, d.microseconds)
(-1, 86399, 999999)

d = timedelta(days = 100, hours = 10, minutes = 13)
print(d)


#EXERCISE 4
#GIVEN SCRIPT
from datetime import datetime 
# get current date 
datetime_object = datetime.now() 
print(datetime_object) 
print('Type :- ',type(datetime_object)) 

#CREATING SEPARATE FUNCTION
from datetime import datetime 
# get current date
def function(feet, inches):
     feet = 1
     inches = 12
     datetime_object = datetime.now()
     print(datetime_object)
     print('Type :- ', (datetime_object))
     function(feet,inches)

#CREATING DATETIME_OBJECT FUNCTION
from datetime import datetime
# get current date
def datetime_object(feet, inches):
    feet = 1
    inches = 12
    datetime_object = datetime.now()
    print(datetime_object)
    print('Type :- ',type(datetime_object))
    datetime_object(feet, inches)
