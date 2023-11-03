from functools import reduce


def calculate_mean(input_data: list[float]) -> float:
    return float(sum(input_data)) / float(len(input_data))


def calculate_variance(input_data: list[float]) -> float:
    mean = calculate_mean(input_data)
    variance = sum(map(lambda elem: (elem - mean) ** 2, input_data))
    return variance


def calculate_line_slope(x_list: list[float], y_list: list[float]) -> float:
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
    x_mean, y_mean = calculate_mean(x_list), calculate_mean(y_list)
    line_y_intercept = y_mean - line_slope * x_mean
    return line_y_intercept
