# Author: Kartik Sah
# Year: 2018
# Topic: Map, Filter Function

def area(radius):
    return 3.14*(radius**2)

radii = [1.,2.,3.,4,5.]
area_cm = list(map(area,radii))
print(area_cm)

# No need to loop over the area function for each radius in the radii list
# map() return a map object , thus useful for larger computations

# Using lambda to change to mm

area_mm_func = lambda data: data*10.0
area_mm = list(map(area_mm_func,area_cm))
print(area_mm)

# Now we want only the area that greater than average area
import statistics
avg = statistics.mean(area_cm)

area_greater_avg = filter(lambda data: data > avg, area_cm)
print(list(area_greater_avg))
