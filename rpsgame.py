import random



def play():
    c_choice = random.choice(["rock", "paper", "scissor"])
#    print(c_choice)
    h_choice_number = int(input("What is your choice? 1. Rock, 2. Paper or 3. Scissor?: "))
    if (h_choice_number == 1):
        h_choice = "rock"
    if (h_choice_number == 2):
        h_choice = "paper"
    elif (h_choice_number == 3):
        h_choice = "scissor"

    if (c_choice == h_choice):
        print(f"TIED!! Computer picked {c_choice} you picked {h_choice}")
    else:
        decide(c_choice, h_choice)

def decide(c, h):
    # r>s, s>p, p>r
    if (c == "rock" and h == "scissor" or c == "scissor" and h == "paper" or c == "paper" and h == "rock"):
        print(f"You LOST!! Computer picked {c}, you picked {h} try again")
    else:
        print(f"You WIN!! Computer picked {c}, you picked {h}")


play()
