# search() method

import re
hand = open('D:\list.txt')
for line in hand:
      
     if re.search('^Python', line) :
              print(line)
