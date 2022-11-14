import numpy as np


def get_relative_frequency(abs_freq):
    """
    Obtain relative frequencies from data.
    relative_frequency = absolute_frequency / sum(absolute_frequency)

    Args:
        abs_freq : absolute frequency (floats, as list)

    Returns:
        rel_freq : relative frequency (floats, as list)
    """

    rel_freq = abs_freq / np.sum(abs_freq)

    return rel_freq


def get_poisson_probs(mean, count):
    """
    Obtain Poisson probabilities for a given set of data.

    Args:
        mean : mean of the data, as float
        count : a list of counts (random discrete variables), as integers

    Returns:
        P, Poisson probabilities, as floats list
        with length that corresponds to the length of the counts list.
    """
    P = []

    for i in range(0, len(count)):
        P.append((mean ** count[i]) / np.math.factorial(count[i]) * np.exp(- mean))

    return P


