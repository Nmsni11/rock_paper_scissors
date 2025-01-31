def rock_paper_scissors():
    choices = ["rock", "paper", "scissors"]
    player = input("Choose rock, paper, or scissors: ").lower()
    computer = random.choice(choices)
    print(f"Computer chose: {computer}")
    if player == computer:
        print("It's a tie!")
    elif (player == "rock" and computer == "scissors") or \
         (player == "scissors" and computer == "paper") or \
         (player == "paper" and computer == "rock"):
        print("You win!")
    else:
        print("You lose!")
