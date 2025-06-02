import random

def main():
    print("Welcome to the Color Guessing Game!")
    colors = ["red", "blue", "green", "yellow", "orange", "purple", "pink", "brown", "black", "white"]
    secret_color = random.choice(colors)
    # Uncomment below to debug the secret color
    # print(f"(Debug) Secret color is: {secret_color}")

    attempts = 0
    while True:
        guess = input("Guess the color (or type 'quit' to exit): ").strip().lower()
        if guess == 'quit':
            print(f"Thanks for playing! The color was '{secret_color}'.")
            break

        attempts += 1

        if guess not in colors:
            print("That's not a valid color in the game. Try again.")
            print(f"Colors you can guess: {', '.join(colors)}")
            continue

        if guess == secret_color:
            print(f"Congratulations! You guessed the correct color '{secret_color}' in {attempts} attempts.")
            break
        else:
            print("Wrong guess. Try again!")

if __name__ == "__main__":
    main()