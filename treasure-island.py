print("Welcome to treassure island game :")
move_left_right = input("you can move? R or L ")



if move_left_right == "R":
    print("game over")
elif move_left_right == "L":
    swim = input("you can go W or S ")
    if swim == "S":
        print("game over")
    elif swim == "W":
        color = input("which color or door R, B, or Y")
        if color == "R" or "B":
            print("game over")
        if color == "Y":
            print("you won")
