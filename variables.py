cars=100
passengers=140
space_in_a_car=4.0
drivers=30
cars_not_driven=cars-drivers
cars_driven=drivers
average_passenger_per_car=passengers/cars_driven
carpool_capcity=cars_driven*space_in_a_car


print"there are", cars, "cars available."
print"there are", drivers, "drivers available."
print"there will be", cars_not_driven, "empty cars today."
print"we can transport", carpool_capcity, "people today."
print"we have", passengers, "to carpool today."
print"we need to put about", average_passenger_per_car, "in each car."