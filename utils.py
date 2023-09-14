def reverse_string(txt: str) -> str:
    """
    reverse a given string
    E.g. "abc" -> "cba"
    @param txt - the input string
    @return the input string in reverse
    """
    return txt[::-1]

def reversed(val: int) -> int:
    """
    reverse a given number
    E.g. "123" -> "321"
    @param val - value to be reversed
    @return the value val in reverse
    @throws TypeError if the input is not integer
    @throws ValueError if the input is negative 
    """

    if(type(val) != int):
        raise TypeError("this function only accept an integer")
    
    if(val < 0):
        raise ValueError("Can't reverse negative digit, that will make negative sign appear at the end")
    
    number_in_string = str(val)
    reversed_string = reverse_string(number_in_string)
    return int(reversed_string)

def formatter(val: int) -> int:
    """
    format a number to binary and octal
    E.g. 10 -> "0b1010", "0o12"
    @param val - value to be formatted
    @return tuple, string of number in binary then in octal
    @throws TypeError if the input is not integer
    """
    if(type(val) != int):
        raise TypeError("This function only accept an integer")
    
    return bin(val), oct(val)