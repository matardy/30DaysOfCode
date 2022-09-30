import numpy as np
from datetime import date 

def distribute_time(start_date:str, end_date:str,hours):
    start_date = start_date.split('/')
    end_date = end_date.split('/')
    start_date = [int(i) for i in start_date]
    end_date = [int(i)for i in end_date]

    start = date(start_date[2],start_date[1], start_date[0])
    end = date(end_date[2],end_date[1], end_date[0])
    
    return hours/np.busday_count(start,end)



