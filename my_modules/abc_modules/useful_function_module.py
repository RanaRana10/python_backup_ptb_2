

'''
Here i will keep some defines some function and then
i will call it in other cases and it will do some works
- find_int_from_string
'''

def find_int_from_string(text):
    """
    Finds all integer numbers in a string by splitting the string.
    Args:
    - text (str): The input string to search for numbers.
        
    Returns:
    list: A list of integer numbers found in the string.
    """
    numbers = []
    for word in text.split():
        if word.isdigit():
            numbers.append(int(word))
    return numbers if numbers else None  # Return None if no integers found
