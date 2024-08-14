import random
import math

lower = int(input("enter lower bound: "))
upper = int(input("enter upper bound: "))

x = random.randint(lower, upper)
total_chances = math.ceil(math.log(upper - lower + 1, 2))
print("\n\tyou've only", total_chances, "chances to guess the integer\n")

count = 0
flag = False

while count < total_chances:
    count += 1

    guess = int(input("guess a number: "))

    if x == guess:

        print("you did it in", count, "try")

        flag = True
        break
    elif x > guess:
        print("too small")
    elif x < guess:
        print("too high")

if not flag:
    print("\nthe number is %d" % x)
    print("\tbetter luck")

