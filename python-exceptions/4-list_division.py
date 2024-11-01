#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            value_1 = my_list_1[i]
            value_2 = my_list_2[i]
            result.append(value_1 / value_2)
        except IndexError:
            print("out of range")
            result.append(0)
        except TypeError:
            print("wrong type")
            result.append(0)
        except ZeroDivisionError:
            print("division by 0")
            result.append(0)
        finally:
            if i >= len(my_list_1) or i >= len(my_list_2):
                continue
    return result

if __name__ == "__main__":
    my_list_1 = [10, 20, 30]
    my_list_2 = [2, 10, 0]
    print(list_division(my_list_1, my_list_2, 5))
