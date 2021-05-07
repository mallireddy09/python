
##  Datetime

#Dates

-> A date in Python is not a data type of its own, 
   but we can import a module named datetime to work
    with dates as date objects.

#Example
-> Import the datetime module and display the current date.

import datetime
x = datetime.datetime.now()
print(x)
# The date contains year, month, day, hour, minute, second, and microsecond.
-> 2021-05-07 10:33:04.978418

-----------------------------------------------------------------------------------------------------------------------------------

# Creating Date Objects
-> To create a date, we can use the datetime() 
   class (constructor) of the datetime module.
-> The datetime() class requires three parameters 
   to create a date: year, month, day.
-> The datetime() class also takes parameters for time and 
   timezone (hour, minute, second, microsecond, tzone), but they are optional, 
   and has a default value of 0, (None for timezone).

# Example
Create a date object:

import datetime
x = datetime.datetime(2019, 4, 15)
print(x)

->2019-04-15 00:00:00 

-----------------------------------------------------------------------------------------------------------------------------------

## The datetime module has many methods to return information about the date object.
# strftime() Method
-> The datetime object has a method for formatting date objects into readable strings.
-> The method is called strftime(), and takes one parameter, format, to specify 
   the format of the returned string:

#Example
Display the name of the month:

import datetime
x = datetime.datetime(2019, 4, 15)
print(x.strftime("%B"))

-> April
---------------------------------------------------------------------------------

# Return the year and name of weekday:

import datetime
x = datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))

-> 2021
   Friday

-----------------------------------------------------------------------------------------------------------------------------------

# datetime module has many methods to return information about the date object.

#Directive	Description	                                                    Example
	
%a	        Weekday, short version	                                        Mon	
%A	        Weekday, full version	                                           Monday	
%w	        Weekday as a number 0-6, 0 is Sunday	                            5	
%d      	  Day of month 01-31	                                              15	
%b      	  Month name, short version	                                     April	
%B	        Month name, full version	                                        April	
%m	        Month as a number 01-12	                                        04	
%y	        Year, short version, without century	                            19	
%Y	        Year, full version	                                              2019	
%H	        Hour 00-23	                                                    23	
%I	        Hour 00-12	                                                    11	
%p	        AM/PM	                                                          PM	
%M	        Minute 00-59	                                                    15	
%S	        Second 00-59	                                                    15	
%f	        Microsecond 000000-999999	                                     548515	
%z	        UTC offset	                                                    +0100	
%Z	        Timezone	                                                       CST	
%j	        Day number of year 001-366	                                     365	
%U	        Week number of year, Sunday as the first day of week, 00-53	    52	
%W	        Week number of year, Monday as the first day of week, 00-53	    52	
%c	        Local version of date and time	                                  Mon April 15 23:15:00 2019	
%x	        Local version of date	                                           04/15/19	
%X	        Local version of time	                                           23:15:15	
%%	        A % character	                                                 %	
%G	        ISO 8601 year	                                                 2019	
%u	        ISO 8601 weekday (1-7)	                                        5	
%V	        ISO 8601 weeknumber (01-53)	                                     18

------------------------------------------------------------------------------------------------------------------------------------------------