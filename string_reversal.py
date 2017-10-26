def reverse_string(input_string):
    '''
    Function returns the reversed version of string given
    input_string: String
    Returns String
    '''
    reversed_input = ''
    index = -1
    for char in input_string:
        reversed_input += input_string[index]
        index += -1
    return reversed_input
