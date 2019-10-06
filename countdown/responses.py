"""File that contains various responses to the player."""

RULES: str = f"""
    You will be given 6 numbers and a goal number.
    
    Your task: to use the 6 numbers to get as close to the
    goal number as possible.
    
    You may add, subtract, multiply, and divide the given numbers, 
    but the result MUST be an integer. You don't have to use all
    of the numbers, but you can't use any numbers that haven't
    been given.
    
    Give your solution as an algebraic expression (e.g. 5 * 6 + 9).
    You may use parentheses.
    
    You have 60 seconds in each round. Good luck!
"""


def START_ROUND(round_num, cards, goal) -> str:
    return f"""
    Round {round_num}:
    
    Your cards are {[card for card in cards]}.
    Your goal is {goal}.
    You have 60 seconds.
    """


INVALID_INPUT: str = f"""
    Your response was invalid! Please try again in the next 
    round.
"""


def CORRECT_ANSWER(expression, result):
    return f"""
    Congratulations!
    You submitted {expression} = {result}, which was exactly
    correct.
    """


def INCORRECT_ANSWER(expression, result, goal_expression, goal_result):
    return f"""
    You submitted {expression} = {result}.
    Our solution was {goal_expression} = {goal_result}.
    You were {abs(result - goal_result)} away!
    """


CONTINUE_PLAYING: str = f"""
    Would you like to play again? (y/n)
"""


END_GAME: str = f"""
    Thanks for playing!
"""
