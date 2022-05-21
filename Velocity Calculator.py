#This program aids to calculate acceleration while converting miles to meters.



print("\n         Acceleration Calculator")

#Create variable of velocity
#Ask user to enter the velocity in miles
v = float(input("\nPlease enter the velocity in miles per hour: "))
    
#Create variable of time
#Ask user to enter the time in seconds
t = float(input("\nPlease enter the time in seconds: "))

#Identify the conversions necessary from miles to meters
#Assign the equation for acceleration
MPH2MPS = (1609/3600)
a = MPH2MPS * v/t

#Display all entered variables
#Show the result at the end with proper decimal spacing
print("\nThe acceleration required by the vehicle to reach a velocity of",v,
      "miles per hour\nin",t,"seconds is:{:8.2f}".format(round(a,1)),"meters per second squared.")
