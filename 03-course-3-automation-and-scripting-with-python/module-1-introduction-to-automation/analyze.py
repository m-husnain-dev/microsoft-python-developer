# Python analyze_errors.py
import sys

# Read lines containing "error" from standard input (provided by subprocess)
for line in sys.stdin:
  # Process each error line
  print(f"Found: {line.strip()}")

print("Finished analyzing errors.")