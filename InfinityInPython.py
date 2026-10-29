'''
In Python, float('inf') represents positive mathematical infinity. It is a special floating-point value that is conceptually greater than any other finite number.




You use float('-inf') (negative infinity) when you need a baseline value that is guaranteed to be smaller than any other number. 

Important Note =>  float('inf') acts as the ultimate maximum.

Important Note => float('-inf') acts as the ultimate minimum.




1. Finding the Maximum Value in a Dataset

When you are loop-searching for the highest number in a collection, you need a starting comparison baseline. If you initialize your tracker to 0, your code will break if the dataset contains only negative numbers. Initializing to float('-inf') ensures that any real number will be larger and successfully overwrite the baseline.

'''


# Find the highest score, even if they are all negative
highest_score = float('-inf')
scores = [-50,-22,-90,-15]
for score in scores:
    if score > highest_score:
        highest_score = score
print(highest_score)



print("\n")

# 1. Basic Behavior & Comparisons
positive_inf = float('inf')
negative_inf = float('-inf')

print(positive_inf>99999999999) # True
print(negative_inf<-9999999999) # True

import math
print(math.inf == float('inf')) # True

print("\n")

# Finding the Minimum Value in a Dataset: 
lowest_price = float('inf')
prices = [25,14,32,9]
for price in prices:
    if price < lowest_price:
        lowest_price = price

print(lowest_price)
        



















