import time

from hanoi import hanoi

# change this to change the number of disks in the game
numDisks = 10

startTimeHanoi = time.time()

hanoi(numDisks, "Start Rod", "Destination Rod", "Auxiliary Rod")

endTimeHanoi = time.time()

totalTimeHanoi = endTimeHanoi - startTimeHanoi

print("Hanoi took", totalTimeHanoi, "seconds with", numDisks, "disks.")
