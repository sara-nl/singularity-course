# Script to print Date and Time

from datetime import datetime

now = datetime.now()

mm = str(now.month)

dd = str(now.day)

yyyy = str(now.year)

hour = str(now.hour)

mi = str(now.minute)

ss = str(now.second)

print ("=====================================================================")
print ("Hello, you are running the Python3 script to print the date and time" )
print ("=====================================================================")

print ("Date: " + mm + "/" + dd + "/" + yyyy + " Time: " + hour + ":" + mi + ":" + ss)
