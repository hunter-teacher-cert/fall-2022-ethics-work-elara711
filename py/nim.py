# NIM
# Erwin Lara
# CSCI 77800 Fall 2022
# attirbution: I worked with Parmanand to fix errors

#set nubmer of player 
player = 1

#set number of objects
stones = '12'
print("The number of stones is ", stones)

while True:
    #valid move
    print("Player ", player)
    while True:
        move = int(input ("How many stones do you want to take? (1, 2 or 3)"))
        if move in [1,2,3] and move < int(stones):
            break
        print("This is not permitted, try again")
    #update the state
    stones = int(stones)-move

    #show the state
    print("The number of stones is  ", stones)
    
    #check the win status - win, lose
    if stones == 1:
        print("PLAYRE ", player, "Wins!")
        break
    
    #switch the players
    if player == 1:
        player = 2
    else:
        player = 1
        
print("GAME OVER!!!.")
