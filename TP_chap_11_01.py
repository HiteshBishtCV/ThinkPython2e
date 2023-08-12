"""Code to read word.txt and store then as keys in dict and comparing speed of 
list (using bisect) method and in operator( hashtable) for dictionary"""

import time

fin = open("words.txt")
keys = fin.read().splitlines()
# using fromkeys
di = dict.fromkeys(keys)

def is_in_dict(dic, target):
    """Checks if target is in dict"""
    if target in dic:
        print(f"{target} in dictionary")
        return 
    
    print(f"{target} not in dictionary")

start_time = time.time()
is_in_dict(di,"zymurgies")
end_time = time.time()
print(f"Time for execution: {end_time-start_time}")