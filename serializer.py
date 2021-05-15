from delorean import Delorean
import json

d = Delorean().datetime
print("Normal datetime value", d, "Type: ", type(d))

d_string = d.isoformat()
print ("serialized datetime value", d_string, "Type: ", type(d_string))

d_str = str(d)
print("serialized datetime value with str method", d_str, "Type: ", type(d_str))
