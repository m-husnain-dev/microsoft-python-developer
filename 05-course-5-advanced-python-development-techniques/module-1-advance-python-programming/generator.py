import sys
import io
from contextlib import contextmanager

@contextmanager
def suppress_stdout():
    """Temporarily suppresses stdout."""
    original_stdout = sys.stdout
    sys.stdout = io.StringIO()
    try:
        yield
    finally:
        sys.stdout = original_stdout

# Example usage:
with suppress_stdout():
    print("This won't be displayed.")

print("This will be displayed.")