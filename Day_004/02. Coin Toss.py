

### INSTRUCTIONS:

#You are going to write a virtual coin toss. It will randomly tell the user "Heads" or "Tails"
import random
test_seed = int(input("Create a seed number: \n"))
random.seed(test_seed)

prob = random.randint(0, 1)

if prob == 0:
    print("Tails")
else:
    print("Heads")
