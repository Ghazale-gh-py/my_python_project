import re

txt = "The rain in Spain"
x = re.search("G", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")