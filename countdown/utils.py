"""File that contains various utility functions."""


def is_valid_subsequence(sequence, subsequence_candidate) -> bool:
    i = 0
    for num in sequence:
        if i >= len(subsequence_candidate):
            return True

        if subsequence_candidate[i] == num:
            i = i + 1

    return i >= len(subsequence_candidate)


def timed_input(text: str, time_limit):
    """
    Get a user's input, but with a time limit.

    Reference: https://stackoverflow.com/questions/15528939/python-3-timed-input

    :param text: text to be displayed to user
    :param time_limit: time (in seconds) the user has to respond
    :return: user's response, or None if they don't respond
    """
    pass
