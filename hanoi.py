# In Tower of Hanoi, there are always 3 rods from left to right:
# the starting rod, where all the disks start the game from
# the auxiliary rod, which we can use to follow the rules
# the destination rod, which we want to move all the disks to
# Rules:
# - Only one disk can move at a time
# - Only the uppermost disk of a rod can be moved
# - No disk may be placed on top of a smaller disk

def hanoi(numberOfDisks, startRod, destinationRod, auxiliaryRod):
    # if the number of disks is only one, the only move we need to do
    # is move the disk from the start rod to the destination rod
    if numberOfDisks == 1:
        print("Moving disk 1 from", startRod, "to", destinationRod)
        return
    
    hanoi(numberOfDisks - 1, startRod, auxiliaryRod, destinationRod)
    print("Moving disk", numberOfDisks, "from", startRod, "to", destinationRod)
    hanoi(numberOfDisks - 1, auxiliaryRod, destinationRod, startRod)
