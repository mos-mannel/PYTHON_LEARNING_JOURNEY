

print("Welcome to Treasure Island ! Your mission is to find the treasure.")

start_point = str(input("You are at a crossed road. Where do you want to go? Left or Right \n")).lower()
if start_point == "left":
    swim_wait = str(input("will you swim or wait?. \n")).lower()
    if swim_wait == "wait":
        door = str(input("Which door do you want to enter?  Red, Yellow or Blue \n")).lower()
        if door == "yellow":
            print("YOU WIN")
        else:
            print("You've entered the door of no return, GAME OVER")
    else:
        print("You've entered a pool full of crocodiles, GAME OVER")
else:
    print("You missed your way, GAME OVER")