#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False

if __name__ == "__main__":
    if not safe_print_integer(89):
        print("School is not an integer")
    if not safe_print_integer(-89):
        print("School is not an integer")
    if not safe_print_integer("School"):
        print("School is not an integer")
