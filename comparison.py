from delorean import Delorean
import datetime

naive_d1 = Delorean(datetime=datetime.datetime(2021, 5, 15), timezone='UTC').naive
naive_d2 = Delorean(datetime=datetime.datetime(2021, 6, 15, 5), timezone='UTC').naive
naive_d3 = Delorean(datetime=datetime.datetime(2021, 5, 15), timezone='US/Pacific').naive
naive_d4 = Delorean(datetime=datetime.datetime(2021, 5, 15, 7), timezone='UTC').naive
print("naive_d1 == naive_d2 -", naive_d1 == naive_d2) # output False because of the hour added to naive_d2
print("naive_d2 > naive_d1 -", naive_d2 > naive_d1) # naive_d2 is a farther date than naive_d1 
print("naive_d3 == naive_d4 -", naive_d3 == naive_d4) # Even though the the timezones are different adding the 7 hours to naive_d4 makes time equal hence, True
 

d1 = Delorean(datetime=datetime.datetime(2021, 5, 15), timezone='UTC')
d2 = Delorean(datetime=datetime.datetime(2021, 5, 15, 5), timezone='UTC')
d3 = Delorean(datetime=datetime.datetime(2021, 5, 15, 1),timezone='Africa/Lagos')
d4 = Delorean(datetime=datetime.datetime(2021, 5, 15), timezone='UTC')
print("d1 == d3 -", d1 == d3) # Even though the the timezones are different adding the 1 hour to d3 makes time equal hence, True
print("d2 > d4 -", d2 > d4)  # adding 5 hours to d2 made it a farther date hence, True

