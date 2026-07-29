"""External performance verification for the Beta function.

This file is not part of the submitted numerical core. It uses Python's timing
library only to reproduce the benchmark described in the D2 presentation.
"""

import time

from beta_core import beta_function


INPUTS = [
    (0.1, 0.2),
    (1.0, 1.0),
    (9.0, 12.0),
    (100.0, 300.0),
    (1000.0, 1.0),
]
RUNS_PER_INPUT = 1000
WARMUP_RUNS = 20
REQUIREMENT_MS = 100.0
PDF_REPORTED_MAX_MS = 0.129


for x_value, y_value in INPUTS:
    for _ in range(WARMUP_RUNS):
        beta_function(x_value, y_value)

maximum_time_ms = 0.0

for x_value, y_value in INPUTS:
    for _ in range(RUNS_PER_INPUT):
        start_ns = time.perf_counter_ns()
        beta_function(x_value, y_value)
        elapsed_ms = (time.perf_counter_ns() - start_ns) / 1_000_000
        maximum_time_ms = max(maximum_time_ms, elapsed_ms)

total_calls = len(INPUTS) * RUNS_PER_INPUT

print(f"Documented inputs: {len(INPUTS)}")
print(f"Timed calls: {total_calls}")
print(f"Maximum observed in submitted PDF: {PDF_REPORTED_MAX_MS:.3f} ms")
print(f"Maximum observed in this run: {maximum_time_ms:.6f} ms")
print(f"Performance requirement: less than {REQUIREMENT_MS:.0f} ms")
print("Result:", "PASS" if maximum_time_ms < REQUIREMENT_MS else "FAIL")
