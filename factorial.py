import timeit
import matplotlib.pyplot as plt


def fact(number):
    if number == 0:
        return 1
    else:
        return number * fact(number-1)


def main():
    input_size = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    time_taken = []
    for input_ in input_size:
        start = timeit.default_timer()
        ans = fact(input_)
        running_time = timeit.default_timer() - start
        time_taken.append(running_time)
        print(ans)
        print("Input Size {} \nRunning Time in Seconds: %.10f \n\n".format(input_) % running_time)
    plt.plot(time_taken, input_size)
    plt.xlabel("Time Taken")
    plt.ylabel("Input size")
    plt.show()


if __name__ == '__main__':
    main()
