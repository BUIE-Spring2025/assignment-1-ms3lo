def int_to_roman(num):
    """
    Convert an integer to a Roman numeral.

    :param num: Integer value between 1 and 3999 inclusive.
    :return: A string representing the Roman numeral of the integer.
    """
    letter_list = [I,V,X,L,C,D,M]
    decimal_list = [1000,500,100,50,10,5,1]
    total_decimal = 0
    for i in range(num):
        total_decimal += 1

