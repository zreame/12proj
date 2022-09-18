import random

options =   {
            "r":"rock", 
            "p":"paper", 
            "s":"scissors"
            }

def play() :
    computer = random.choice(["r", "p", "s"])
    user = input("Enter r for rock, p for paper, s for scissors: ").lower()

    if user not in options :
        return "Invalid!"
    
    if computer == user :
        return f"Computer chose {options[computer]}. Tie!"

    if is_win(computer, user) :
        return f"Computer chose {options[computer]}. You win!"
    
    return f"Computer chose {options[computer]}. You lose!"
    
def is_win(computer, user) :
    # p > r, r > s, s > p
    return (user == "p" and computer == "r") or (user == "r" and computer == "s") or (user == "s" and computer == "p")

print(play())
