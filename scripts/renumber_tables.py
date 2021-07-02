import os
import re

# Number to begin with
begin = 0

def increment_one():
    global begin
    
    begin += 1
    
    return begin

# Path to existing tables
directory = r'C:\inetpub\wwwroot\SITES\hectaad365\Tables'
# Path to save new tables
directory2 = r'C:\inetpub\wwwroot\SITES\hectaad365\TablesNew'

for filename in os.listdir(directory):

    with open(directory + '\\' + filename, 'r+', encoding='utf-8') as f:

        content = f.read()
        
        find = re.sub("table [0-9]+", lambda exp: "table " + str(increment_one()), content, flags=re.M)
        
        if find:
            o = open(directory2 + '\\' + filename, 'w', encoding='utf-8')
            
            o.write(find)
            
            o.close()
