from delorean import Delorean

d = Delorean().datetime
print(type(d), d)
d_string = d.isoformat()
print ("serialized date", "Type: ",type(d_string), d_string)