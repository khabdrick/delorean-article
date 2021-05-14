from delorean import Delorean
from datetime import timedelta 

dt_tm = Delorean()
dt_tm += timedelta(days=5)

print(dt_tm)


dt_tm_ago = Delorean()
dt_tm_ago -= timedelta(days=3)

print("Date 3 days ago is ", dt_tm_ago)