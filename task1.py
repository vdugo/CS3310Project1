import random
import time

from mergesort import mergesort
from quicksort import quicksort



# generate a list of random numbers
numbers = []

# change the second number in this range to change the number of elements in the array
for index in range(0, 250000):
    # the random integers can be from 0 to 1 million
    randomInt = random.randint(0, 1000000 + 1)
    numbers.append(randomInt)


numbersCopy = list(numbers)

startTimeMergesort = time.time()
mergesort(numbers,0,len(numbers) - 1)
endTimeMergesort = time.time()
totalTimeMergesort = endTimeMergesort - startTimeMergesort

print(totalTimeMergesort, "seconds to complete mergesort.")

startTimeQuicksort = time.time()
quicksort(numbersCopy,0,len(numbersCopy) - 1)
endTimeQuicksort = time.time()
totalTimeQuicksort = endTimeQuicksort - startTimeQuicksort

print(totalTimeQuicksort, "seconds to complete quicksort.")
