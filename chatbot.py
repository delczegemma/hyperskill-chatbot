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

def old_enough_to_count():
    print('Now I will prove to you that I can count to any number you want.')

    any_number = int(input())
    for i in range(any_number + 1):
        print(f"{i} !")

    print('Completed, have a nice day!')

# Now we can use these functions
greet("Aid", 2026)
remind_name()
age_guessing()
old_enough_to_count()