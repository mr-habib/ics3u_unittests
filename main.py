# Mr. Habib
# 05/28/2021
# Calculating the average!

def calculate_average(numbers, n=-1):
    """Calculate the mean average of the first n numbers of a list of numbers
    
    Args:
        numbers: A list of numbers
        n: How many numbers of the list to include in the average calculation.
    
    Returns:
        The mean average of the first n numbers of the numbers list
    """
    # Deal with the default argument
    up_to = n 
    if up_to < 0 or up_to > len(numbers):
        up_to = len(numbers)
    # / Deal with the default argument

    # Actually find the average of the first n numbers
    the_sum = 0
    for i in range(up_to):
        the_sum = the_sum + numbers[i]

    if up_to == 0: up_to = 1

    return round(the_sum / up_to, 2)

