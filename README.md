# Beta Function Calculator - SOEN 6011 D2

This project implements the Beta function calculator for F6:

```text
B(x, y) = Gamma(x) Gamma(y) / Gamma(x + y), for x > 0 and y > 0
```

## D2 scope

- Implements the numerical core from scratch in Python.
- Uses no `math` module and no numerical library.
- Implements the subordinate operations `natural_log`, `exponential`, and
  `log_gamma` in `beta_core.py` with arithmetic and iteration.
- Provides a Tkinter graphical user interface.
- Handles missing, nonnumeric, nonfinite, zero, negative, overflow, and
  underflow cases with field-specific messages.
- Supports repeated calculations, input swapping, clearing, keyboard commands,
  and calculation history.

Tkinter is used only for the required graphical user interface. Python's
`float` conversion and string formatting are used for input and output.

## Run

Python 3 with Tkinter is required.

```bash
python3 beta_function_gui.py
```

The application does not depend on an IDE. Keep `beta_core.py` and
`beta_function_gui.py` in the same directory.

## Demo checks

Use these cases in the GUI:

| Purpose | Input | Expected result or behaviour |
|---|---|---|
| Known value | `x = 1`, `y = 1` | `1` |
| Known value | `x = 2`, `y = 3` | approximately `0.0833333333333` |
| Symmetry | `x = 3`, `y = 2` | same result as `B(2, 3)` |
| Scientific notation | `x = 1e2`, `y = 3e2` | finite positive result |
| Nonnumeric | `x = abc` | field-specific input error |
| Domain error | `x = -2` | `x must be greater than zero` |
| Recovery | correct the input and calculate again | application remains open |

## Numerical design

`natural_log` reduces its argument to `[1, 2)` and evaluates an atanh-based
series. `exponential` reduces its argument using powers of two and evaluates a
Taylor series. `log_gamma` shifts positive inputs to at least 8 using the Gamma
recurrence and then applies a Stirling series. The Beta value is evaluated in
the logarithmic domain to avoid directly multiplying large Gamma values.

Floating-point range still applies. The program reports a numeric-range error
when the final result cannot be represented as a nonzero finite float.

## Repository

Public repository URL: pending publication.

## Author

Wei Huang  
SOEN 6011, Concordia University  
Summer 2026
