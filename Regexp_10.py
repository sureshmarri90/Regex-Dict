# Reg Exp
# separates alternate possibilities
# Search "|"

import re
s='Hello,world'
if re.search(r"(Hello|Hi|Pogo)",s):
                print("The String 's' contains at least one Hello|Hi|Pogo")
else:
                print("The String 's' not contains at least one Hello|Hi|Pogo")
                
      
      
            
 
      
            
       
