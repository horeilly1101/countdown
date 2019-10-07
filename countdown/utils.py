"""File that contains various utility functions."""


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
