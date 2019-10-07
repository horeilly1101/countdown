"""File that contains various responses to the player."""

RULES: str = f"""
    WELCOME TO COUNTDOWN

    You will be given 6 numbers and a goal number.
    
    Your task: Use the 6 numbers to get as close to the
    goal number as possible.
    
    You may add, subtract, multiply, and divide the given numbers, 
    but the result MUST be an integer. You don't have to use all
    of the numbers, but you can't use any numbers that haven't
    been given. The order of the numbers in your answer does not 
    matter.
    
    Give your solution as an algebraic expression (e.g. 5 * 6 + 9).
    You may use parentheses. 
    
    Good luck! Press ENTER to begin.
    """


def START_ROUND(round_num, cards, goal) -> str:
    return f"""
    Round {round_num}:
    
    Your cards are {[card for card in cards]}.
    Your goal is {goal}.
    """


PARSE_ERROR: str = """
    Your answer was unable to be parsed! Please try again in the
    next round.
    """


INVALID_NUMBERS_ERROR: str = """
    Your answer included number(s) that weren't given! Please try
    again in the next round.
    """

EVALUATION_ERROR: str = """
    Your input expression did not evalute to an integer! Please try
    again in the next round.
    """


def CORRECT_ANSWER(expression, result) -> str:
    return f"""
    Congratulations!
    You submitted {expression} = {result}, which was exactly
    correct.
    """


def INCORRECT_ANSWER(expression, result, goal_expression, goal_result) -> str:
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
