import random
import time

from hanoi import hanoi

startTimeHanoi = time.time()

hanoi(16, "Start Rod", "Destination Rod", "Auxiliary Rod")

endTimeHanoi = time.time()

totalTimeHanoi = endTimeHanoi - startTimeHanoi

print("Hanoi took", totalTimeHanoi, "seconds")