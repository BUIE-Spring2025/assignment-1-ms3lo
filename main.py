def int_to_roman(num):
    """
    Convert an integer to a Roman numeral.

    :param num: Integer value between 1 and 3999 inclusive.
    :return: A string representing the Roman numeral of the integer.
    """
    letter_list = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    decimal_list = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]


    roman_letter_output = ''

    for i in range(len(decimal_list)):
        
        while decimal_list[i] < num:
            num == num - decimal_list[i]

            roman_letter_output += letter_list[i]
    
    return roman_letter_output

int_to_roman()



    


