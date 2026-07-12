#!/usr/bin/env python3
"""
Execute the TX-0 Consistency Testing Suite and capture results to a file.
"""

import subprocess
import sys
import time

print("=" * 80)
print("TX-0 CONSISTENCY TEST EXECUTION")
print("=" * 80)
print(f"Start time: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")

# Run the main test suite
result = subprocess.run(
    [sys.executable, "engine2_512.py"],
    capture_output=True,
    text=True,
    timeout=300
)

# Print output
print(result.stdout)
if result.stderr:
    print("STDERR:", result.stderr)

# Save to results file
with open("test_results.txt", "w") as f:
    f.write(result.stdout)
    if result.stderr:
        f.write("\n\nSTDERR:\n")
        f.write(result.stderr)

print(f"\nEnd time: {time.strftime('%Y-%m-%d %H:%M:%S')}")
print("Results saved to test_results.txt")
print("=" * 80)

sys.exit(result.returncode)
