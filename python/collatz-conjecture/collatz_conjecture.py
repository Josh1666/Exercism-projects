"""A module defining how many steps a number takes to reach 1 using collatz sequence"""

def steps(number):
    """Return the number of steps to reach 1 using collatz sequence"""
    if number <= 0:
        raise ValueError("Only positive integers are allowed")

    step_count = 0
    # Continue collatz rule until 1
    while number != 1:
        if number % 2 == 0:
            number = number // 2
        else:
            number = (number * 3) + 1
        step_count += 1
        
    return step_count