import pandas as pd
import numpy as np

days = [['Mon',20],['Tue',21],['Wed',22],['Thu',23],['Fri',24],['Sat',25],['Sun',26]]


df = pd.DataFrame(days,index=[1,2,3,4,5,6,7],columns =['Days','Date'])

print(df)

