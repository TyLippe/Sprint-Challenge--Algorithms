#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n), reasoning as n increases the runtime will increase at a the same rate


b) O(n^2), reasoning the function will run n, n times.


c) O(n), reasoning function is recursive and will run n times 

## Exercise II

For an algorthim like this I would build it where the user inputs the amount of floors (n). I would then use a binary search approach, we will drop the egg in the middle floor (mid = f // 2), if the egg survives then we will work to the right of the mid, if the egg breaks we will work on the left of the mid. Either direction we will do the same search and find the new mid of the split floors, drop the egg again until we find a floor where the egg survives the fall and f+1 it breaks. We will lose a good amount of eggs but not as much as we would in a linear search. Time complexity should be  O(log(n)) because we are running half of n operations. 

import random

#define where egg will break
def egg_floor(n):
    egg = random.randrange(n + 1)
    egg_break(n, egg)

#function that will check where egg does not break
def egg_break(n, egg):
    floor = n
    if floor == 0:
        return 0
    mid = floor // 2
    drop = floor[mid]
    if egg == floor-1:
        last_safe = floor - 1
        return last_safe
    elif egg > floor:
        return egg_break(floor[:mid], egg)
    else:
        return egg_break(floor[mid:], egg)
    


