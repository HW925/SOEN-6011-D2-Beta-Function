"""From-scratch numerical core for the Beta function.

This module intentionally avoids Python's math module and numerical libraries.
Natural logarithm, exponential, and log-gamma are implemented with arithmetic
and iteration.
"""


LN_2 = 0.69314718055994530942
HALF_LN_2_PI = 0.91893853320467274178
MAX_FLOAT = 1.7976931348623157e308
MAX_EXP_ARGUMENT = 709.782712893384
MIN_EXP_ARGUMENT = -744.4400719213812
SERIES_TOLERANCE = 1.0e-16


class InputValidationError(ValueError):
    """Raised when an input is missing or outside the function domain."""


class NumericRangeError(ArithmeticError):
    """Raised when a result cannot be represented as a finite Python float."""


def absolute_value(value):
    """Return the nonnegative magnitude of a real number."""
    if value < 0.0:
        return -value
    return value


def is_finite(value):
    """Return True when value is neither infinity nor NaN."""
    return value == value and -MAX_FLOAT <= value <= MAX_FLOAT


def natural_log(value):
    """Compute ln(value) using range reduction and an atanh-based series."""
    if not is_finite(value) or value <= 0.0:
        raise InputValidationError(
            "Natural logarithm requires a finite value greater than zero."
        )

    reduced = value
    power_of_two = 0

    while reduced >= 2.0:
        reduced *= 0.5
        power_of_two += 1

    while reduced < 1.0:
        reduced *= 2.0
        power_of_two -= 1

    ratio = (reduced - 1.0) / (reduced + 1.0)
    ratio_squared = ratio * ratio
    term = ratio
    denominator = 1.0
    series_sum = 0.0

    while denominator <= 199.0:
        addition = term / denominator
        series_sum += addition
        if absolute_value(addition) <= SERIES_TOLERANCE:
            break
        term *= ratio_squared
        denominator += 2.0

    return 2.0 * series_sum + power_of_two * LN_2


def exponential(value):
    """Compute exp(value) using range reduction and a Taylor series."""
    if not is_finite(value):
        raise NumericRangeError("The exponential argument must be finite.")
    if value > MAX_EXP_ARGUMENT:
        raise NumericRangeError("The result is too large to represent.")
    if value < MIN_EXP_ARGUMENT:
        raise NumericRangeError(
            "The Beta result is positive but smaller than the minimum nonzero "
            "Python float, so it cannot be represented."
        )

    reduced = value
    scale = 1.0
    half_ln_2 = 0.5 * LN_2

    while reduced > half_ln_2:
        reduced -= LN_2
        scale *= 2.0

    while reduced < -half_ln_2:
        reduced += LN_2
        scale *= 0.5

    term = 1.0
    series_sum = 1.0
    index = 1.0

    while index <= 80.0:
        term *= reduced / index
        series_sum += term
        if absolute_value(term) <= SERIES_TOLERANCE:
            break
        index += 1.0

    result = series_sum * scale
    if result == 0.0 or not is_finite(result):
        raise NumericRangeError(
            "The Beta result is outside the nonzero finite Python float range."
        )
    return result


def log_gamma(value):
    """Compute ln(Gamma(value)) using recurrence and a Stirling series."""
    if not is_finite(value) or value <= 0.0:
        raise InputValidationError(
            "Log-gamma requires a finite value greater than zero."
        )

    shifted = value
    recurrence_correction = 0.0

    while shifted < 8.0:
        recurrence_correction -= natural_log(shifted)
        shifted += 1.0

    inverse = 1.0 / shifted
    inverse_squared = inverse * inverse
    inverse_cubed = inverse * inverse_squared
    inverse_fifth = inverse_cubed * inverse_squared
    inverse_seventh = inverse_fifth * inverse_squared
    inverse_ninth = inverse_seventh * inverse_squared
    inverse_eleventh = inverse_ninth * inverse_squared

    correction = (
        inverse / 12.0
        - inverse_cubed / 360.0
        + inverse_fifth / 1260.0
        - inverse_seventh / 1680.0
        + inverse_ninth / 1188.0
        - 691.0 * inverse_eleventh / 360360.0
    )

    stirling = (
        (shifted - 0.5) * natural_log(shifted)
        - shifted
        + HALF_LN_2_PI
        + correction
    )
    return stirling + recurrence_correction


def beta_function(x_value, y_value):
    """Return B(x, y) for finite positive real inputs."""
    if not is_finite(x_value):
        raise InputValidationError("x must be finite.")
    if not is_finite(y_value):
        raise InputValidationError("y must be finite.")
    if x_value <= 0.0:
        raise InputValidationError("x must be greater than zero.")
    if y_value <= 0.0:
        raise InputValidationError("y must be greater than zero.")

    combined = x_value + y_value
    if not is_finite(combined):
        raise NumericRangeError("x + y is outside the finite numeric range.")

    log_result = (
        log_gamma(x_value)
        + log_gamma(y_value)
        - log_gamma(combined)
    )
    return exponential(log_result)
