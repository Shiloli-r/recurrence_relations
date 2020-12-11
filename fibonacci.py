import timeit
import matplotlib.pyplot as plt


def fibonacci_sequence(no_of_terms):
    # first two terms
    f1 = 0
    f2 = 1
    count = 0
    while count < no_of_terms:
        print('Term {} => {}'.format(count + 1, f1))

        nth = f1 + f2
        f1 = f2
        f2 = nth
        count = count + 1


def main():
    time_taken = []
    input_ = []
    loop = int(input("Number of times to run the algorithm: "))
    for i in range(loop):
        no_of_terms = int(input("Number of terms: "))
        start_time = timeit.default_timer()
        fibonacci_sequence(no_of_terms)
        stop_time = timeit.default_timer()
        running_time = stop_time - start_time
        time_taken.append(running_time)
        input_.append(no_of_terms)
        print('******\nInput Size {}\nTime %.10f\n******\n'.format(no_of_terms) % running_time)
    print("Time: ", time_taken)
    print("input: ", input_)
    plt.plot(time_taken, input_)
    plt.xlabel("Time Taken")
    plt.ylabel("Input Size")
    plt.show()


if __name__ == "__main__":
    main()
