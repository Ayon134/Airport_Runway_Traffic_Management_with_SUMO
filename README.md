# Airport_Runway_Traffic_Management_with_SUMO
This is a project for CSE474 (Simulation)
We have taken Hartsfield-Jackson Atlanta International Airport as our vision.

# How to run?
In order to run and see whats hapenning just install SUMO simulator and run the .cfg file suing SUMO GUI. 

# Variable
1. Number of plane on runway
2. Number of plane on air want to land
3. Number of plane on request to takeoff next
Unfortunately, we could not get a good dataset so we created by ourselves, how...[see dataset point]?
So, we had to work with only 2 variable time and length of runway. [Only using time as independant variable was giving less accuracy but adding another variable made accuracy better.]

# Dataset
1. As mentioned, we have taken Hartsfield-Jackson Atlanta International Airport as our vision, there 2500 planes can takeoff or land in any regular day and it has 4 runways
2. So, technically in every 2min 30 sec a plane take off or land in this airport. Keeping this in mind we created a dataset.
3. In DATASETs folder you will find random.py that generates the csv file as our dataset.
What the dataset carry?
4. The dataset carries few days of plane landing or taking off time in msec. [assuming 100ms = 1sec, just to make things easy] So, it has 24 hours cycle for few days.
5. Apart time you will find T/L which means if it is landing[0] or taking off[1].
6. Next, lane length and width, which are also taken from source but as time or T/L it was random as well.

# What is happening?
1. 2 model we run on the dataset, and they gave different accuracy, we took the best one
2. Based on the prediction we applied on SUMO but it was hardcoaded. [Best way to manupulate SUMO is using TraCI]

To learn more please follow the link.[it will be public after the final 😁]

This project is still under development. Still you are free to use codes and data.

# Thank you
