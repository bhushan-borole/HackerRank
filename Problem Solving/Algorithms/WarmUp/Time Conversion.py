# https://www.hackerrank.com/challenges/time-conversion/submissions

import re
def time_conversion(s):
    list = s.split(":")
    
    if re.search('PM', list[2]):
        if int(list[0])<12:
            new_hour = 12 + int(list[0])
            list[0] = str(new_hour)
            
    if re.search('AM', list[2]):
        
        if int(list[0])==12:
            list[0] = "00"
            
        
        
        
    list[2] = list[2][0:2]
    print(":".join(list))
        
if __name__ == '__main__':    
    s = input()
    time_conversion(s)
