print("The more of this there is, the less you see. What is it?")

secret_word = "darkness"
guess = ""

while guess != secret_word:
    guess = input("Enter your guess: ")

print("You win!")