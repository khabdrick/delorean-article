from delorean import Delorean
import datetime

dt_tm = Delorean()
dt_tm += datetime.timedelta(days=5)

print("Date 3 days from now is ", dt_tm)


dt_tm_ago = Delorean()
dt_tm_ago -= datetime.timedelta(days=3)

print("Date 3 days ago is ", dt_tm_ago)


ch_day = Delorean(datetime=datetime.datetime(2021, 5, 27), timezone='utc')
print(ch_day)
