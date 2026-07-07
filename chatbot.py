def greet(bot_name, birth_year):
    print(f"Hello! My name is {bot_name}.")
    print(f"I was created in {birth_year}.")


def remind_name():
    your_name = input("Please, remind me your name: ")
    # reading a name
    print(f"What a great name you have, {your_name}!")

def age_guessing():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')
    remainder3 = int(input())
    remainder5 = int(input())
    remainder7 = int(input())
    # reading all remainders
    your_age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105

    print(f"Your age is {your_age}; that's a good time to start programming!")

# Now we can use these functions
greet("Aid", 2026)
remind_name()
age_guessing()