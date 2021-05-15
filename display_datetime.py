from delorean import Delorean   #importing the  library  we installed previously

dt_tm = Delorean() #Function that carries all the date and time properties
change_tz = dt_tm.shift('Africa/Lagos')
print ("date and time = ",dt_tm)

dt = change_tz.date 
print ("date = ",dt)

tm = change_tz.datetime.time()
print ("time = ",tm)

nxt_fri = dt_tm.next_friday()
print ("date for next week friday is = ", nxt_fri)



