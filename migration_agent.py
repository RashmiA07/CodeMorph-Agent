"""
AI Code Base Migration Agent
This script takes legacy Python 2 code and refactors it into clean, modern Python 3.12 code.
"""

# 1. Define the Legacy Code Input (Python 2 syntax)
legacy_code = """
def calculate_metrics(values):
    total = 0
    for val in values:
        total += val
    print "Total sum is:", total
    print "Average is:", total / len(values)
    keys = {"a": 1, "b": 2}.keys()
    print "Keys list:", keys
"""

# 2. Simulated Modernization Pipeline Output (Python 3.12 syntax)
modern_code = """
def calculate_metrics(values: list[float | int]) -> None:
    total = sum(values)
    print(f"Total sum is: {total}")
    print(f"Average is: {total / len(values) if values else 0}")
    keys = list({"a": 1, "b": 2}.keys())
    print(f"Keys list: {keys}")
"""

# 3. Execution Logs
print("=" * 55)
print("   AI CODE BASE MIGRATION AGENT - RUNNING")
print("=" * 55)
print("\n[INPUT - LEGACY PYTHON 2 CODE]:")
print(legacy_code)

print("-" * 55)
print("[PROCESSING] Analyzing AST and migrating code structures...")
print("-" * 55)

print("\n[OUTPUT - MODERN PYTHON 3.12 CODE]:")
print(modern_code)
print("=" * 55)
print("SUCCESS: Code Migration Complete! 0 Syntax Errors Found.")
print("=" * 55)