from delorean import Delorean
from datetime import timedelta 

dt_tm = Delorean()
dt_tm += timedelta(days=3)

print(dt_tm)
