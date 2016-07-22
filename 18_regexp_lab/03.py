#comited by Shlomit
import re

def changePlace(text):
   regex= "(^[^,]+),([^,]),(.*)"
   res = re.search(regex,text)
   if res is not None:
       print res.group(2)+ "," + res.group(1) + "," + res.group(3)
 
#changePlace("s,b,y,4")