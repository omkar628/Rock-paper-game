while True:
    import random 
    choices=["rock","paper","sicissor"]
    computer = random.choice(choices)
    player = None
    while player not in choices:
        player = input("rock,paper,sicissor:?").lower()
    if player==computer:
        print("player:",player)
        print("computer:",computer)
        print("tie")
    elif player=="rock":
        if computer=="paper":
            print("player:",player)
            print("computer:",computer)
            print("you lose")
        if computer=="sicissor":
            print("player:",player)
            print("computer:",computer)
            print("you won")
    elif player=="paper":
        if computer=="rock":
            print("player:",player)
            print("computer:",computer)
            print("you won")
        if computer=="sicissor":
            print("player:",player)
            print("computer:",computer)
            print("you lose")
    elif player=="sicissor":
        if computer=="paper":
            print("player:",player)
            print("computer:",computer)
            print("you won")
        if computer=="rock":
            print("player:",player)
            print("computer:",computer)
            print("you lose")
    else:
        print("something went wrong")

    play_again= input("play again (yes/no)")

    if play_again!="yes":
        print("thankyou for playing" )
        break
print("byii")


    

    
        
    

