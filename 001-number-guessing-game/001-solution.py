import random 

def random_numgenerator():
    random_num = random.randint(0, 100)
    return random_num

def user_guess():
    user_input = int(input("Guess a number between 0 and 100: "))
    return user_input


losing = True
actual_num = random_numgenerator()
print(f"the actual number is {actual_num}")

while losing:
    guess_num = user_guess()

    if guess_num > actual_num:
        print("Too High guess again")
    elif guess_num < actual_num:
        print("Too Low guess again")
    else:
        print("You are Correct")
        losing = False



