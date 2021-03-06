from delorean import Delorean   #importing the  library  we installed previously

dt_tm = Delorean() #Function that carries all the date and time properties

print ("date = ",dt_tm)  

tm = Delorean().datetime.time()  #new
print ("time = ",tm)  #new

#display naive datetime
naive_dt_tm = dt_tm.naive #new
print ("Naive datetime is",naive_dt_tm)  #new

change_tz = dt_tm.shift('Africa/Lagos')
print ("date and time after changing timezone = ",change_tz)


nxt_fri = dt_tm.next_friday()
print ("date for next week friday is = ", nxt_fri)


# Date for Two Fridays ago
last_2_tues = dt_tm.last_fiday(2)
print ("date for 2 Fridays ago", last_2_tues)

# Get Two Fridays from now at midnight
next_2_fris_midnight = dt_tm.next_friday(2).midnight
print ("Two Fridays from now at midnight is ", next_2_fris_midnight)