import os
items_shown = 0

for files in os.walk():
  for _file in files:
    if size = os.path.getsize(full_path) > 1000000:
      print(f"Size: {size}b - File: {full_path}")   
    items_shown += 1
    
    if items_shown > 10:
        break
     
