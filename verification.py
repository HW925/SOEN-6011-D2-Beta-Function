"""External accuracy verification for the Beta function.

This script is not part of the submitted numerical core. It compares values
from beta_core.py with independent mathematical identities and high-precision
reference values.
"""

from decimal import Decimal, getcontext

from beta_core import beta_function


getcontext().prec = 80

TOLERANCE = Decimal("1e-10")
PI_REFERENCE = Decimal(
    "3.1415926535897932384626433832795028841971693993751058209749445923"
)


def integer_factorial(value):
    """Return value! using integer arithmetic."""
    result = 1
    for factor in range(2, value + 1):
        result *= factor
    return result


def relative_error(computed, reference):
    """Return |computed - reference| / |reference|."""
    computed_decimal = Decimal.from_float(computed)
    return abs(computed_decimal - reference) / abs(reference)


reference_values = [
    ("B(1, 1)", 1.0, 1.0, Decimal(1)),
    ("B(2, 3)", 2.0, 3.0, Decimal(1) / Decimal(12)),
    ("B(0.5, 0.5)", 0.5, 0.5, PI_REFERENCE),
    (
        "B(100, 300)",
        100.0,
        300.0,
        Decimal(integer_factorial(99))
        * Decimal(integer_factorial(299))
        / Decimal(integer_factorial(399)),
    ),
]

print(f"{'Input':<16} {'Computed value':>22} {'Relative error':>18}  Result")
print("-" * 68)

all_passed = True

for label, x_value, y_value, reference in reference_values:
    computed = beta_function(x_value, y_value)
    error = relative_error(computed, reference)
    passed = error <= TOLERANCE
    all_passed = all_passed and passed

    print(
        f"{label:<16} {computed:>22.15g} {float(error):>18.3e}  "
        f"{'PASS' if passed else 'FAIL'}"
    )

print("-" * 68)
print(f"Required relative-error tolerance: {float(TOLERANCE):.1e}")
print("Overall result:", "PASS" if all_passed else "FAIL")
