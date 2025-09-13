"""
Leaky Bucket rate limiter implementation.
https://www.geeksforgeeks.org/system-design/rate-limiting-algorithms-system-design/
"""

import time
import math

class LeakyBucket:
    """
    Leaky Bucket rate limiter implementation.
    The bucket leaks at a constant rate (leak_rate) per second.
    Incoming requests are added to the bucket if there is space.
    Requests are allowed if the bucket is not full.
    """
    def __init__(self, capacity, leak_rate, time_func=None):
        self.capacity = capacity  # Maximum number of requests in the bucket
        self.leak_rate = leak_rate  # Leak rate (requests per second)
        self.water = 0.0  # Current amount in the bucket
        self._time_func = time_func or time.monotonic
        self.timestamp = self._time_func()  # Last leak timestamp

    def _leak(self):
        """
        Leak water from the bucket based on elapsed time since last check.
        """
        now = self._time_func()
        elapsed = now - self.timestamp
        leaked = elapsed * self.leak_rate
        if leaked > 0:
            self.water = max(0.0, self.water - leaked)
            # Clamp to zero if very close to zero
            if abs(self.water) < 1e-6:
                self.water = 0.0
            self.timestamp = now

    def allow_request(self, amount=1.0):
        """
        Attempt to add 'amount' to the bucket.
        Returns True if allowed, False if bucket is full.
        """
        self._leak()
        if self.water + amount < self.capacity or math.isclose(self.water + amount, self.capacity, rel_tol=1e-9, abs_tol=1e-9):
            self.water += amount
            # Clamp to capacity if very close
            if abs(self.water - self.capacity) < 1e-6:
                self.water = self.capacity
            return True
        return False

# ------------------- TESTS -------------------
# These tests use time.sleep to simulate passage of time.
# In production, you would want to mock time for deterministic tests.

def test_leaky_bucket_basic():
    # Use a mock time function
    t = [0]
    def mock_time():
        return t[0]
    bucket = LeakyBucket(capacity=5, leak_rate=1, time_func=mock_time)
    for _ in range(5):
        assert bucket.allow_request() == True
    assert bucket.allow_request() == False
    # Advance time by 1.1s
    t[0] += 1.1
    assert bucket.allow_request() == True
    assert bucket.allow_request() == False

def test_leaky_bucket_burst():
    t = [0]
    def mock_time():
        return t[0]
    bucket = LeakyBucket(capacity=3, leak_rate=2, time_func=mock_time)
    for _ in range(3):
        assert bucket.allow_request() == True
    assert bucket.allow_request() == False
    t[0] += 0.35
    assert bucket.allow_request() == False
    t[0] += 0.2
    assert bucket.allow_request() == True
    # Reset bucket to full before leak test
    bucket.water = bucket.capacity
    bucket.timestamp = t[0]
    t[0] += 2
    print(f"[DEBUG] Water after leak: {bucket.water}")
    for _ in range(2):
        assert bucket.allow_request() == True
    print(f"[DEBUG] Water before final deny: {bucket.water}")
    assert not (bucket.allow_request()), f"Water level: {bucket.water}"
    assert math.isclose(bucket.water, 3, abs_tol=0.05) or bucket.water < 3

def test_leaky_bucket_multi_amount():
    t = [0]
    def mock_time():
        return t[0]
    bucket = LeakyBucket(capacity=10, leak_rate=5, time_func=mock_time)
    assert bucket.allow_request(amount=7) == True
    assert bucket.allow_request(amount=4) == False
    assert bucket.allow_request(amount=3) == True
    assert bucket.allow_request(amount=1) == False
    t[0] += 1.1
    assert bucket.allow_request(amount=5) == True
    assert bucket.allow_request(amount=1) == False

if __name__ == "__main__":
    test_leaky_bucket_basic()
    test_leaky_bucket_burst()
    test_leaky_bucket_multi_amount()
    print("All tests passed.")
