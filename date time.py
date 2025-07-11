import datetime
import time
while True:
    C_time = datetime.datetime.now()
    formatted_time = C_time.strftime("%I:%M:%S %p")  
    print(formatted_time)
    time.sleep(1)
    # %p gives AM/PM
    # %I hour
    # %M minits
    # %S seconds
    
