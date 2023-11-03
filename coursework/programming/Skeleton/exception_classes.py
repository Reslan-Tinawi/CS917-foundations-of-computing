class ColumnNotFoundException(Exception):
    # Exception message set by value
    def __init__(self, value):
        self.parameter = value

    # Exception message to be printed
    def __str__(self):
        return self.parameter


class InvalidDateTypeException(Exception):
    # Exception message set by value
    def __init__(self, value):
        self.parameter = value

    # Exception message to be printed
    def __str__(self):
        return self.parameter


class OutOfRangeDateException(Exception):
    # Exception message set by value
    def __init__(self, value):
        self.parameter = value

    # Exception message to be printed
    def __str__(self):
        return self.parameter


class InvalidDateRangeException(Exception):
    # Exception message set by value
    def __init__(self, value):
        self.parameter = value

    # Exception message to be printed
    def __str__(self):
        return self.parameter
