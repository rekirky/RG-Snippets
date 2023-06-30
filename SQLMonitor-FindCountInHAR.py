import tkinter as tk
import json
from tkinter import filedialog
from haralyzer import HarParser
import re

# Create a Tkinter root window
root = tk.Tk()
root.withdraw()


# Path to the HAR file
har_file_path = filedialog.askopenfilename()
print(har_file_path)

# Create a HarParser object and parse the HAR file
with open(har_file_path,'r',encoding='utf8') as f:
    har_parser = HarParser(json.loads(f.read()))

data = har_parser.har_data

print(data.keys())

pattern=r"([^,]+Count[^,]+)"

for i in data['entries']['resonse']['content']:
    print(i)
    
        

    #matches = re.findall(pattern,i)
#for match in matches:
#print(match)
    


