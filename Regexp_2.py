# Reg Exp
# Search_[.]

import re
s='Hello.'
if re.search(r".....[.]",s):
      print(s+" has length>=5 and ends with a .")
else:
      print('Not matched')
       
