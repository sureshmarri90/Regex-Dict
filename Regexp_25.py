# split()
# The Regex Version

#this is the last example

import re
line = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
y=re.findall('^From .*@([^ ]*)',line)
print(y)
print(str(y))


             
