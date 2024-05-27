import random as r
print("A game")
def rock_paper_scissors(lose, win):
    rock = '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    '''

    paper = '''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    '''

    scissors = '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    '''
    user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
    if user_choice not in [0, 1, 2]:
        return "The data was wrong, try again"
    random_choice = r.randint(0, 2)
    if user_choice == 0:
        print(rock)
        if random_choice == 0:
            print(rock)
            return "It's a draw"
        elif random_choice == 1:
            print(paper)
            return "You lost"
        else:
            print(scissors)
            return "You won"
    elif user_choice == 1:
        print(paper)
        if random_choice == 0:
            print(rock)
            return "You won"
        elif random_choice == 1:
            print(paper)
            return "It's a draw"
        else:
            print(scissors)
            return "You lost"
    elif user_choice == 2:
        print(scissors)
        if random_choice == 0:
            print(rock)
            return "You lost"
        elif random_choice == 1:
            print(paper)
            return "You won"
        else:
            print(scissors)
            return "It's a draw"


user, robot = 0, 0

while True:
    print(rock_paper_scissors(robot, user))
    restart = input("Do you want to continue? y, n?")
    if restart != "y":
        break

