import random

print("Welcome to the SAINT PETERSBURG PARADOX GAME!\n\n")
print("""***Saint Petersburg Paradox Game Explanation***
1. A fair coin is tossed repeatedly until HEADS show up.
2. The pay off is determined by the number of times the user plays the game.
3. The minimum pay is $2, if HEAD appears on the n-th toss, then the payoff is $(2**n)

***Theoretical Explanation of this paradox***
This game has/ gives the opportunity to the user to earn in trillions, the EXPECTED VALUE is INFINITE.
But yet, most people are not willing to pay a large amount to participate in the game.

SO now, lets see how much you will be willing to pay and how much you will earn with this PARADOX STIMULATION GAME.""")


def paradox():
    global payoff
    global toss
    payoff = 1
    toss = 1
    while True:
        coin = random.choice(["HEADS", "TAILS"])
        print("---->", coin)
        if coin == "HEADS":
            print("Its HEADS... Time to end the game...")
            break
        else:
            payoff *= 2  # You get 2**n times
            toss += 1  # here, toss = n
        return payoff, toss


def gain_loss(fee):
    paradox()
    gain = payoff - fee
    loss = fee - payoff
    print(f"You got HEADS ofter {toss} many tries\nYou won ${payoff}")
    if payoff > fee:
        print(f"\nYESSS!! You made a profit of ${gain}.\n\t\tPaying ${fee} was a good strategy.")

    else:
        print(
            f"Oh no... Unfortunately, you are in loss of ${loss}.\n\t\tFee you payed ${fee}\n\t\tPayoffs is ${payoff}")


def game():
    global fee
    fee = float(input("\n\nEnter the fee you are willing to pay: $"))
    gain_loss(fee)
    again = input("\n\nDo you want to play again (Y/N): ").upper()
    if again == "Y":
        game()


game()
