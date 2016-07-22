#commited by Shlomit
import re

def ToCamel(text):
   return re.sub(r'_([a-z])',lambda m: m.group(1).upper(),text)

def FromCamel(text):
   return re.sub("([a-z])([A-Z])","\g<1>_\g<2>",text).lower()

#print fromCamel("noMoreSallWePart")
#print ToCamel("no_more_shall_we_part")