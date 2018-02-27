# search()

import re
a= open('D:\EMP1.txt')
for l in a:
       if re.search('CLERK',l) :
                      print(l)
       else:
              print("none")
