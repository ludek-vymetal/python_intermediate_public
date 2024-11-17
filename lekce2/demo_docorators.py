from datetime import datetime


def disable_during_day(func):
    def wrapper():
        if 22 <= datetime.now().hour < 7:
            func()
        else:
            print("Je den, nerus me..")
    return wrapper

@disable_during_day
@disable_during_day
def say_something():
    print("Hello world")

@disable_during_day
def say_always():
    print("Hello ALWAYS")



say_something()
say_always()
