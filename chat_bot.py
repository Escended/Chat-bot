def greet(bot_name, birth_year):
    print(f'Hello! My name is {bot_name}.')
    print(f'I was created in {birth_year}.')


def remind_name():
    print('What is your name?...')
    name = input()
    print(f'Pleasure to make your acquaintance, {name}.')


def guess_age():
    print('I bet I can guess your age...')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print(f"Your age is {age} that's a good time to start programming!")


def count():
    print('Now I will prove to you that I can count to any number you want.')

    num = int(input())
    current = 0
    while current <= num:
        print(f'{current} !')
        current += 1


def test():
    print("Let's test your programming knowledge.")
    print("What is the time complexity of binary search?")
    print("1. O(logN).")
    print("2. O(N).")
    print("3. O(1).")
    print("4. O(n^2).")
    ans = int(input())
    while ans != 1:
            print("Please, try again")
            ans = int(input())

    print('Completed, have a nice day!')


def end():
    print('Congratulations, have a nice day!')


greet('Gosu', '2020')  # change it as you need
remind_name()
guess_age()
count()
test()
end()
