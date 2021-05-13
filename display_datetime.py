from delorean import Delorean   #importing the  library  we installed previously

dt_tm = Delorean() #Function that carries all the date and time properties
# print ("date and time = ",dt_tm)

dt = Delorean().date 
print ("date = ",dt)

tm = Delorean().datetime.time()
print ("time = ",tm)

change_tz = dt_tm.shift('Africa/Lagos')
print ("date and time = ",dt_tm)