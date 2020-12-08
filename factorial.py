import timeit


def fact(number):
    if number == 0:
        return 1
    else:
        return number * fact(number-1)


def main():
    start = timeit.default_timer()
    ans = fact(10)
    print(ans)
    running_time = timeit.default_timer() - start
    print("Running Time in Seconds: %.10f" % running_time)


if __name__ == '__main__':
    main()
