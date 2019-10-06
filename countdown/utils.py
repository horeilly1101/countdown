"""File that contains various utility functions."""
from threading import Timer


def is_valid_subsequence(sequence, subsequence_candidate) -> bool:
    """
    :param sequence: input sequence
    :param subsequence_candidate: the subsequence candidate
    :return: whether or not the subsequence candidate is a valid
        subsequence of the input sequence.
    """
    i = 0
    for num in sequence:
        if i >= len(subsequence_candidate):
            return True

        if subsequence_candidate[i] == num:
            i = i + 1

    return i >= len(subsequence_candidate)


def timed_input(input_text: str, time_limit):
    """
    Get a user's input, but with a time limit. Return None if they don't
    respond within the time limit.

    Reference: https://stackoverflow.com/questions/15528939/python-3-timed-input

    :param text: text to be displayed to user
    :param time_limit: time (in seconds) the user has to respond
    :return: user's response, or None if they don't respond
    """
    answer_on_time = True
    timer = Timer(time_limit, print, ["Time's up! Press Enter to continue."])
    timer.start()
    answer = input(input_text)
    timer.cancel()
    return answer

if __name__ == "__main__":
    timed_input("hello", "bye", 5)
