# SOEN 6011 D2 Presentation Script

Target duration: approximately 6 minutes 30 seconds.

## Slide 1 - Title

Hello, my name is Wei Huang. This is Deliverable 2 for function F6, the Beta
function. I will present the from-scratch numerical implementation, the Tkinter
interface, the version-control evidence, and the revised requirements.

## Slide 2 - Scope and dependency chain

D2 increments my D1 solution. D1 selected the log-gamma identity but used
`math.lgamma` and `math.exp` through a textual interface. D2 preserves that
mathematical decision while replacing the library operations with my own
functions and the TUI with a Tkinter GUI.

"From scratch" allows input, output, arithmetic, exception handling, and the
required GUI services, but no mathematical or numerical library. This is an
iterative increment of the earlier baseline, as described in the course notes.

## Slide 3 - From-scratch architecture

The GUI sends the two text inputs to field-specific validation. Valid finite
positive values are passed to `beta_function`, which computes the result and
adds it to the history.

The core has three subordinate operations. `natural_log` uses range reduction
and a series. `log_gamma` uses recurrence and a Stirling correction.
`exponential` converts the logarithmic result back to a Beta value. The core
does not import `math`, SciPy, or NumPy.

Exceptions are recoverable. An invalid value updates the status message, while
the window remains open so the user can correct the field.

## Slide 4 - Numerical method and verification

For natural logarithm, I reduce the argument to the interval from one to two and
use the series shown here. For exponential, I reduce with powers of two and use
a Taylor series.

For log-gamma, I repeatedly apply the Gamma recurrence until the argument is at
least eight, then use Stirling's formula with correction terms. Finally, I
evaluate log Beta as log-gamma of x plus log-gamma of y minus log-gamma of their
sum.

External verification did not add a library dependency to the submitted
program. Three known values have very small relative errors, and the larger
case remains accurate. An unrepresentable result produces a numeric-range error
instead of a misleading zero or infinity.

## Slide 5 - Tkinter GUI and exception recovery

The Tkinter interface has labeled fields, Calculate, Swap, and Clear controls,
a result and status area, and calculation history. Enter calculates and Escape
clears.

The error messages explain both the problem and the correction. Missing input
names the required field. Nonnumeric input gives valid examples. Domain errors
state that the value must be greater than zero. Range errors explain that the
result cannot be represented. After every handled error, the GUI stays open and
ready for corrected input.

The demonstration covers a known value, symmetry, nonnumeric and negative
inputs, recovery, and repeated calculations.

## Slide 6 - Distributed version control

For Problem 6, four purpose-focused commits separate the numerical core, GUI
and recovery, documentation, and repository evidence.

The README explains the function, terminal command, from-scratch boundary,
demo cases, and numerical limits. This is lightweight documentation consistent
with the course notes. The submitted version shows the public repository URL.

## Slide 7 - Updated functional requirements

Problem 7 updates the D1 requirements to match the actual D2 system. The
functional requirements now specify labeled GUI controls, finite positive real
inputs including scientific notation, the three from-scratch numerical
operations, at least ten significant digits in the displayed result, session
history, and the ability to continue after either a result or a handled error.

Terminal prompts and a quit command are replaced by GUI controls, history, and
explicit recovery.

## Slide 8 - Constraints and quality requirements

The constraints make the implementation boundary testable: the GUI shall use
Tkinter, the core shall not call built-in or library mathematical functions,
and the application shall run from a terminal independently of an IDE. Each
handled input error must name the field and the correction.

The quality requirements are measurable. Known values and symmetry use a
relative tolerance of ten to the minus ten. Representable results in the stated
domain must complete within one hundred milliseconds, and the GUI must remain
usable after an error.

## Slide 9 - GAI use

I used OpenAI ChatGPT and Codex and documented the work with CASTROFF. The
context was D2 for F6, the audience was the instructor and TA, and the role was
a software engineering student. Outputs were Python, a README, requirements,
and slides.

For P5, I accepted the recurrence and Stirling approach, revised it by adding
range checks, and rejected direct Gamma multiplication. For P6, I checked that
the proposed commits matched real repository changes and ran the README
commands. For P7, I revised the output by separating functional, constraint,
accuracy, timing, and recovery requirements. All numerical claims were verified
by execution and trusted identities rather than accepted directly from the AI.

## Slide 10 - References

These are the project, course, mathematical, and requirements references.

In summary, D2 replaces the D1 library calls with a verified from-scratch
numerical core, provides a recoverable Tkinter GUI, records the work in version
control, and updates the requirements to describe the implemented system.
Thank you.
