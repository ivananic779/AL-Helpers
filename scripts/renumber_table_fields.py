import os
import re

# Number to begin with
start = 0

begin = start

def increment_one():
    global begin
    
    begin += 1
    
    return begin

# Where are the tables
directory = r'C:\inetpub\wwwroot\SITES\hectaad365\Tables'
# Where to save the changed tables
directory2 = r'C:\inetpub\wwwroot\SITES\hectaad365\TablesNew'

for filename in os.listdir(directory):
    # Reset for every file
    begin = start

    with open(directory + '\\' + filename, 'r+', encoding='utf-8') as f:

        content = f.read()
        
        find = re.sub("field\(([0-9]+)", lambda exp: "field(" + str(increment_one()), content, flags=re.M)
        
        if find:
            o = open(directory2 + '\\' + filename, 'w', encoding='utf-8')
            
            o.write(find)
            
            o.close()
