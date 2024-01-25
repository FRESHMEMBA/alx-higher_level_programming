#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        new_item = 0
        try:
            new_item = my_list_1[i] / my_list_2[i]
        except (ValueError, TypeError):
            print("wrong type")
            # new_item = 0
        except ZeroDivisionError:
            print("division by 0")
            # new_item = 0
        except IndexError:
            print("out of range")
            # new_item = 0
        finally:
            new_list.append(new_item)

    return new_list
