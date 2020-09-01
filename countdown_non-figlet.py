import os
import time


def clear(): return os.system('cls' if os.name == 'nt' else 'clear')


def countdown(_type):
    def countdown1(_func):
        def wrapper():
            maxNum = _func()
            clear()
            for i in range(maxNum, 0, -1):
                print(i)
                time.sleep(1)
                clear()
            print('FINISH')
        return wrapper

    def countdown2(_func):
        def wrapper():
            maxNum = _func()
            clear()
            for i in range(maxNum-1, -1, -1):
                for j in range(9, -1, -1):
                    print(f"{i}.{j}")
                    time.sleep(0.1)
                    clear()
            print('FINISH')
        return wrapper
    types = ['1', '2']
    if _type in types:
        return locals()['countdown'+_type]
    else:
        def errorHandling(_func):
            def wrapper():
                print('Type is not valid. Valid types: '+", ".join(types))
            return wrapper
        return errorHandling


@countdown(input('Enter countdown type: '))
def num():
    clear()
    return int(input('Set Countdown: '))


num()
