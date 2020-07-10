result = []
def order_numbers(list_1):
    if list_1 == []:
        return result
    else:
        for element in range(len(list_1)):
            if list_1[element - 1] >= list_1[element]:
                list_1[element], list_1[element -
                                        1] = list_1[element -
                                                    1], list_1[element]
            else:
                continue
    result.append(list_1[len(list_1) - 1])
    list_1.pop(len(list_1) - 1)
    return order_numbers(list_1)


order_numbers([200, 5, 2, 3, 4, 6, 1, 6, 100,0])
