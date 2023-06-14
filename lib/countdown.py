import time


def countdown(int):
    while int:
        print(f"{int} SECOND(S)!")
        int -= 1

    print("HAPPY NEW YEAR!")


def countdown_with_sleep(int):
    while int:
        print(f"{int} SECOND(S)!")
        int -= 1
        time.sleep(1)
    print("HAPPY NEW YEAR!")


countdown_with_sleep(10)
