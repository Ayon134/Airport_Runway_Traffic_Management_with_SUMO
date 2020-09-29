# let 100ms = 1 sec

import pandas as pd 
import random
import csv

lane_list = []  # empty list for len or runway
time_list = []  # empty list for time 
L_T = []        # empty list for landing or take off
length_list = []# empty list for runway length
width_list = [] # empty list for runway width
i = 0
t = 0           # time starts at 0 msec

while (i <= 70000):            # 3k times iteration
    if (t <= 8640000):         # time starts from 0 after each 24 hours
        for j in range(1,5):   # 4 runway, so 1 to 4 lane itaration 3000 times
            lr = j
            if(lr == 2 or lr == 3):
                length_list.append(6000) # length in feet
                width_list.append(200)   # width in feet
            else:
                length_list.append(13000) # length in feet
                width_list.append(230)    # width in feet
            tr = random.randint(20 , 100) #20 ms to 100ms random choice
            t = t + tr   # time adding
            L_T_r = random.randint(0, 1)  # randomly take 0(land) or 1(take off)
            lane_list.append(lr)
            time_list.append(t)
            L_T.append(L_T_r)
        t = t + random.randint(9300, 10000) # in order to avoid using same lane before 2min
    else:   # time starts from 0 after each 24 hours
        t = 0
    i = i+1

# print(lane_list)
# print(time_list)
 
# Create the dataframe 
df = pd.DataFrame({'Lane'       : lane_list, 
                    'Time(ms)'  : time_list,
                    'L/T'       : L_T,
                    'length_ft' : length_list,
                    'Width_ft' : width_list}) 
df.to_csv('runway_set.csv') # write a csv file
#print(df)  # Print the dataframe 
