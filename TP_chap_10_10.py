def bisect(sorted_list,target):
    
    # Stop condition
    if len(sorted_list)==1:
        if sorted_list[0]==target:
            return 1
        else:
            return None
    
    i = len(sorted_list)//2
    if sorted_list[i]==target:
        return i
    elif sorted_list[i]<target:
       if type(bisect(sorted_list[i:],target))==int:  #idk why if type(bisect(sorted_list[i:],target))!=None is causing problem
            return i+bisect(sorted_list[i:],target)
       else:
           return None
    elif sorted_list[i]>target:
        if type(bisect(sorted_list[:i],target))==int:  
            return bisect(sorted_list[:i],target)
        else:
           return None
    

fin = open("words.txt")
sorted_list = fin.read().splitlines()
import time
start_time = time.time()

print(bisect(sorted_list, "loofs"))
print(time.time() - start_time)
print(bisect(sorted_list, "lancbd"))


