import random
hero = ("bloodmother", "rublick", "juggaunt", "lion", "phonix", )

print('Let play some order characters hero')

play = input("Lets play (Yes/No) \n").lower()
while play == "yes":
    word = random.choice(hero)
    correct = word
    jumble = ""
    while word:
        position = random.randrange(len(word))
        jumble += word[position] +" "
        word = word[:position] + word[(position + 1):]

    print("Your answer: ",jumble)
    points = 100
    guess = input("\nYour answer : ")
    while guess != correct and guess != "":
        print("Sorry, wrong one")
        guess = input("Your answer : ")

    if guess == correct:
        print("Hura, Great one!\n")
        print("Your point: " + str(points))
        play=input("Do you want to play more? (Yes/No) ")
    elif guess == "":
        print("Nope...")
        play=input("Do you want to play again? (Yes/No) ")


print("Thanks for your time")

input("\n\nENTER for exit")