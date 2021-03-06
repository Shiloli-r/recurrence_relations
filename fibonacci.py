import timeit


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
    start_time = timeit.default_timer()
    no_of_terms = int(input("Number of terms "))
    fibonacci_sequence(no_of_terms)
    stop_time = timeit.default_timer()
    running_time = stop_time - start_time
    print('\n******\n\nInput Size {}\nTime %.10f\n\n******'.format(no_of_terms) % running_time)


if __name__ == "__main__":
    main()
