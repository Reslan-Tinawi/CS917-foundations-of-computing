"""
    Statistical functions realted to calculating linear regression
"""
from functools import reduce


def calculate_mean(input_data: list[float]) -> float:
    """Calculates the mean of a list of numbers

    Args:
        input_data (list[float]): list of numbers

    Returns:
        float: mean value
    """
    return float(sum(input_data)) / float(len(input_data))


def calculate_variance(input_data: list[float]) -> float:
    """Calculates the variance for a list of numbers

    Args:
        input_data (list[float]): list of numbers

    Returns:
        float: variance
    """
    mean = calculate_mean(input_data)
    variance = sum(map(lambda elem: (elem - mean) ** 2, input_data))
    return variance


def calculate_line_slope(x_list: list[float], y_list: list[float]) -> float:
    """Given two vectors X and Y, this function calculates the line slope according to the line equation:

    Y = mX + b

    m is the slope of the line

    Args:
        x_list (list[float]): the independent variable
        y_list (list[float]): the dependent variable

    Returns:
        float: the slope of the line
    """
    x_mean, y_mean = calculate_mean(x_list), calculate_mean(y_list)

    # centering x and y vectors by subtracting the mean from each element
    x_centered = list(map(lambda elem: elem - x_mean, x_list))
    y_centered = list(map(lambda elem: elem - y_mean, y_list))

    # taking the sum of products of x_centered[i] and y_centered[i] for i=1..N
    numerator = reduce(lambda x, y: x + y, map(lambda t: t[0] * t[1], zip(x_centered, y_centered)))

    x_variance = calculate_variance(x_list)

    line_slope = numerator / x_variance

    return line_slope


def calculate_line_y_intercept(x_list: list[float], y_list: list[float], line_slope: float) -> float:
    """Calculates the y-intercept of a line

    Args:
        x_list (list[float]): the independent variable
        y_list (list[float]): the dependent variable
        line_slope (float): the slope of the line

    Returns:
        float: the y-intercept of the line
    """
    x_mean, y_mean = calculate_mean(x_list), calculate_mean(y_list)

    # b = Y - mX
    line_y_intercept = y_mean - line_slope * x_mean

    return line_y_intercept
