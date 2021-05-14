from delorean import Delorean
import datetime

dt_tm = Delorean()
dt_tm += datetime.timedelta(days=5)

print("Date 3 days from now is ", dt_tm)


dt_tm_ago = Delorean()
dt_tm_ago -= datetime.timedelta(days=3)

print("Date 3 days ago is ", dt_tm_ago)

present_date = Delorean()
ch_day = Delorean(datetime=datetime.datetime(2021, 5, 27), timezone='UTC') # This is how to insert your own date in Delorean
days_till_ch_day = ch_day - present_date 
print("Days till children day ", days_till_ch_day)
print("Days till children day ",days_till_ch_day.days)  #display only the number of  days

