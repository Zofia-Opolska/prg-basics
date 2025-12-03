###
# The weather station report
#
temp = [
 3, 7, 1, -2, 6, -4, 5, 1, 2, 3,
 4, -1, 0, 2, -1, -2, 5, -2, 7, 2,
 -1, 4, 1, -4, 2, 3, 6, 7, 5, 7
]

# number of mesaurements
mesaurements = len(temp)

# calculates average temperature
temp_total = 0
for x in temp:
   temp_total += x
avg_temp = temp_total/mesaurements

# calculates min and max temp
min_temp = min(temp)
max_temp = max(temp)

# calculates number of days with negative temp
negative_temp = 0
for i in temp:
   if i < 0:
        negative_temp += 1
    
    
    

print('TEMPERATURE REPORT')
print('Month: March')
print('Number of measurements:', mesaurements)
print('Average temperature in the month:', avg_temp)
print('Minimum temperature:', min_temp)
print('Maximum temperature:', max_temp)
print('Number of days with negative temperature:', negative_temp)