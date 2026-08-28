from contextlib import contextmanager

@contextmanager
def custom_timer():
    import time
    start = time.time()
    yield  # Yahan tak __enter__ ka kaam hota hai, iske baad yield ke neeche __exit__
    end = time.time()
    print(f"Time taken: {end - start:.4f} seconds")

# Usage
with custom_timer():
    sum(range(10000000))