import time
print(time.time())
#print(time.gmtime())
def convert_sec(time_in_sec):
    """ converts currents time to time elased from epoch 1 jan 1970 to no of days elapsed and time of day,
    in hrs, min and seconds 
    """
    days_since_epoch = time_in_sec//(24*60*60)
    sec_in_today_after_rem_days = time_in_sec%(24*60*60)
    hrs_in_today = sec_in_today_after_rem_days//(60*60)
    sec_in_today_after_rem_hrs = sec_in_today_after_rem_days%(60*60)
    min_in_today =sec_in_today_after_rem_hrs//60
    sec_in_today = sec_in_today_after_rem_hrs%60
    print(f"No of days since 1 jan 1970 {days_since_epoch} \n hrs {hrs_in_today} \n {min_in_today} \n {sec_in_today}]")

convert_sec(time.time())