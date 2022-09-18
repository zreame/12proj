import random



def user_guess() :
    upper = input("Upper no: ")
    upper = int(upper)
    comp_rand = random.randint(1, upper)
    guess = 0
    while guess != comp_rand :
        guess = input(f"Guess a number between 1 and {upper}: ")
        guess = int(guess)
        if guess > comp_rand : 
            print("Too high, try again.")
        elif guess < comp_rand :
            print("Too low, try again.")
    print("Congrats, you got it!")

def comp_guess() :  
    upper = input("Upper no: ")
    upper = int(upper)
    ans = ''
    low = 1
    high = upper
    while ans != 'c' :
        guess = random.randint(low, high)
        ans = input(f'Guess is {guess}. If correct enter c, else enter l if answer is lower or h if answer is higher: ').lower()
        if ans == 'l' :
            high = guess - 1
        elif ans == 'h' :
            low = guess + 1
    print(f'You got it, answer is {guess}!')




