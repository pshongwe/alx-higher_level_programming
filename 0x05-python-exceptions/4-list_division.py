#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    
    for i in range(list_length):
        try:
            element_1 = my_list_1[i] if i < len(my_list_1) else 0
            element_2 = my_list_2[i] if i < len(my_list_2) else 0
            division_result = element_1 / element_2
        except ZeroDivisionError:
            division_result = 0
            print("division by 0")
        except (TypeError, ValueError):
            division_result = 0
            print("wrong type")
        except IndexError:
            print("out of range")
            break
        finally:
            result.append(division_result)
    return result
