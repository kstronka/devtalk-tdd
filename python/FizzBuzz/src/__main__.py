import sys
from fizzbuzz import fizzbuzz


def print_usage_and_exit():
    print("Usage: python __main__.py <integer>")
    sys.exit(1)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print_usage_and_exit()

    try:
        input = int(sys.argv[1])
        print(fizzbuzz.get_message(input))
    except ValueError:
        print_usage_and_exit()