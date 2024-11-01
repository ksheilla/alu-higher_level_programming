#!/usr/bin/python3
def safe_print_division(a, b):
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        pass
    finally:
        print("Inside result: {}".format(result))
    return result

if __name__ == "__main__":
    print("{} / {} = {}".format(12, 2, safe_print_division(12, 2)))
    print("{} / {} = {}".format(12, 0, safe_print_division(12, 0)))
