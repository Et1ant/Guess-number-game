import random
def get_best_score():
    try:
        with open("record.txt", "r") as f:
            return int(f.read())
    except (FileNotFoundError, ValueError):
        return float('inf')
def save_best_score(score):
    with open("record.txt", "w") as f:
        f.write(str(score))
print("Welcome to guess-number game!")
best_score = get_best_score()
if best_score != float('inf'):
    print(f"Current high score: {best_score} attempts")
else:
    print("No high score yet. Be the first!")
def choose_difficulty():
    while True:
        try:
            choice = int(input("\nChoose difficulty: 1. Easy(10), 2. Medium(5), 3. Hard(3): "))
            if choice == 1: return 10
            if choice == 2: return 5
            if choice == 3: return 3
            print("Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Enter a number.")
attempts_limit = choose_difficulty()
secret_number = random.randint(1, 100)
for i in range(attempts_limit):
    current_attempt = i + 1
    try:
        guess = int(input(f"Attempt {current_attempt}/{attempts_limit}. Take a guess: "))
    except ValueError:
        print("Enter a valid number!")
        continue
    if guess == secret_number:
        print(f" You guessed it! The number was {secret_number}.")
        print(f" NEW HIGH SCORE! Previous was {best_score if best_score != float('inf') else 'none'}")
        save_best_score(current_attempt)
        break
    elif guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")
else:
    print(f"Sorry, you're out of attempts. The number was {secret_number}")


