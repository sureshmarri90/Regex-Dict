# {m,n} Matches the preceding element at least m and not more than n times.
# Search  "{}"

import re
s='Malayalam'
if re.search(r"a{1,4}",s):
      print("The string 's' contains at least one 'a's & max four 'a's. ")
else:
      print("The string 's' does not contains 'a'.")
      

      

