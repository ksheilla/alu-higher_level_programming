#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            print(my_list[i], end="")
            count += 1
        except IndexError:
            break
    print()
    return count


if __name__ == "__main__":
    print(safe_print_list([1, 2, 3, 4], 4))
    print(safe_print_list([1, 2], 2))
    print(safe_print_list([1, 2, 3, 4], 4))
