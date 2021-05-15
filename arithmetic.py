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

d = Delorean(datetime=datetime.datetime(2021, 5, 14, 12), timezone='UTC')
altered_tm = d.replace(hour=10)
altered_dt = d.replace(month=10)
print("Altered time is ", altered_tm)
print("Altered date is ", altered_dt)


trun_min = present_date.truncate('minute')
trun_sec = present_date.truncate('second')

trun_day = present_date.truncate('day')
trun_month = present_date.truncate('month')
print("trun_min = ", trun_min)
print("trun_sec = ", trun_sec)
print("trun_day = ", trun_day)
print("trun_month = ", trun_month)