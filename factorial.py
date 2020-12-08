import time


def fact(number):
    if number == 0:
        return 1
    else:
        return number * fact(number-1)


def main():
    start = time.time()
    ans = fact(100)
    print(ans)
    running_time = time.time() - start
    print("Running Time in Seconds: ", running_time)


if __name__ == '__main__':
    main()
