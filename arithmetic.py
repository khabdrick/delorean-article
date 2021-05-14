from delorean import Delorean
from datetime import timedelta 

dt_tm = Delorean()
dt_tm += timedelta(hours=5)

print(dt_tm)
