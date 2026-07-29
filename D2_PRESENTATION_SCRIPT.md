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

"From scratch" means that the numerical core uses no built-in or library
functions except those permitted for input, output, arithmetic, interface
design, and exception handling. This is an iterative increment of the earlier
baseline.

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

External verification did not add a dependency to the submitted core. Known
values have very small relative errors. Across 5,000 timed benchmark calls, the
maximum observed time was 0.129 milliseconds. An underflow case produces a
helpful range error instead of a misleading zero.

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

For Problem 6, the public GitHub history uses purpose-focused commits. They
separate the numerical core, GUI and recovery, documentation, presentation,
and repository publication.

## Slide 7 - README documentation

The README documents the function and D2 scope, the from-scratch subordinate
operations, and the Tkinter interface. It also gives an IDE-independent terminal
command, reproducible demo cases, the numerical design and floating-point limit,
and the public repository URL. This is lightweight documentation consistent
with the course notes.

## Slide 8 - Updated functional requirements

Problem 7 updates the D1 requirements to match the actual D2 system. The
functional requirements now specify labeled GUI controls, finite positive real
inputs including scientific notation, the three from-scratch numerical
operations, at least ten significant digits in the displayed result, session
history, recovery, and detection of unrepresentable results.

Terminal prompts and a quit command are replaced by GUI controls, history, and
explicit recovery.

## Slide 9 - Constraints and quality requirements

The constraints make the boundary testable: the core may use only the permitted
categories of functions, the interface shall use Tkinter, and supported
exceptions shall not terminate the application.

Known values and symmetry use a relative tolerance of ten to the minus ten. Each
documented benchmark must complete within one hundred milliseconds, and the
interface must remain usable after an error.

## Slide 10 - GAI use

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

## Slide 11 - References

These are the project, course, mathematical, and requirements references.

In summary, D2 replaces the D1 library calls with a verified from-scratch
numerical core, provides a recoverable Tkinter GUI, records the work in version
control, and updates the requirements to describe the implemented system.
Thank you.
