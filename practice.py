# Add up and print the sum of the all of the minimum elements of each inner array:

array = [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]

# The expected output is given by:
# 4 + -1 + 9 + -56 + 201 + 18 = 175

# we will need to access the inner arrays
# inner for loops
# need to compare the value to see which is less
# once we have the lesser value from each array we need to sum them up and print

def compare():
    sum = 0
    for x in array:
        # compare
        sum += min(x)
    return print(sum)
       

print(compare())

# Add up and print the sum of the all of the minimum elements 
# of each inner array. Each array may contain additional arrays 
# nested arbitrarily deep, in which case the minimum value for the 
# nested array should be added to the total.

arr = [
  [8, [4]], 
  [[90, 91], -1, 3], 
  [9, 62], 
  [[-7, -1, [-56, [-6]]]], 
  [201], 
  [[76, 0], 18], 
]





