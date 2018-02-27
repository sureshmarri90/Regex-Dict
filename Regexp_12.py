# Reg Exp
# Search "()"

import re
s='Hello, world.'
obj=re.search(r"(H..).(o..)(...)",s)

if re.search(r"(H..).(o..)(...)",s):
      print("we matched "+ obj.group(1) +" and "+ obj.group(2) +" and "+ obj.group(3))
      
      
