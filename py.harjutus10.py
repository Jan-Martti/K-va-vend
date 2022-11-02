#J.M.O
#02.11.2022
#harjutus10


import re

fh = open("loll.txt")
for line in fh:
    if re.search("^[A-Z0-9]+[A-Z]{1}", line):
         print(line,end='')

print("------------------------------------------")
#kuva korralikud paroolid
fh = open("loll.txt")
for line in fh:
    if re.search("^(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$", line):
         print(line,end='')



