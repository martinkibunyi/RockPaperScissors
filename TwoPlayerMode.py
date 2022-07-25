print("Hello!!!\nWelcome to Rock,Paper,Scissors!!!\n")
player1 = 0
player2 = 0
draw = 0
options = ["a","b","c"]
#A is rock, B is Paper, C is Scissors
while True:
    user1 = input("Player1:Pick A,B or C!!!\nQ to quit!!!\n").lower()
    user2 = input("Player2:Pick A,B or C!!!\nQ to quit!!!\n").lower()
    if user1 == "q" or user2 == "q":
        print("No winner Declared!!!")
        break
    if user1 not in options or user2 not in options:
        print("Enter a valid option!!!")
        continue
    if user1 == "a" and user2 == "c":
        print("Player 1 wins!!!\n")
        player1 +=1
    elif user1 == "b" and user2 == "a":
        print("Player 1 wins!!!\n")
        player1 += 1
    elif user1 == "c" and user2 == "b":
        print("Player 1 winss!!!\n")
        player1 += 1
    elif user1 == "a" and user2 == "a":
        print("You chose the same answer!!!Try again!!!\n")
        draw += 1
    elif user1 == "b" and user2 == "b":
        print("You chose the same answer!!!Try again!!!\n")
        draw += 1
    elif user1 == "c" and user2 == "c":
        print("You chose the same answer!!!Try again!!!\n")
        draw += 1
    else:
        print("Player 2 Wins!!!\n")
        player2 += 1
print("Player 1 won",player1,"times!!!\nPlayer 2 won",player2,"times!!!\n")
print("Goodbye!!!")

