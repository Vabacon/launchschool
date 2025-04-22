# Build a program that asks the user to enter the length and width of a room, in meters,
#  then prints the room's area in both square meters and square feet.
# Note: 1 square meter == 10.7639 square feet

# Need user input for length and width in Meters
# Print the area of the room in Square Meters and Square Feet.

length = int(input('Please enter the length in Meters: '))
width = int(input('Please enter the width in Meters: '))

area_mtsq = (length * width)
area_ftsq = area_mtsq * 10.7638


print(f'{area_mtsq} squared meters.')
print(f'{area_ftsq} squared feet.')