"""
https://www.geeksforgeeks.org/system-design/rate-limiting-algorithms-system-design/
"""

import time
import math

class TokenBucket:
    """
    Token Bucket rate limiter implementation.
    Allows up to 'capacity' tokens in the bucket.
    Tokens are refilled at a rate of 'fill_rate' tokens per second.
    Each request consumes one token.
    """
    def __init__(self, capacity, fill_rate):
        self.capacity = capacity  # Maximum number of tokens in the bucket
        self.tokens = capacity    # Current number of tokens
        self.fill_rate = fill_rate  # Tokens added per second
        self.timestamp = time.monotonic()  # Last refill timestamp

    def _add_new_tokens(self):
        """
        Add new tokens to the bucket based on elapsed time since last check.
        Only whole tokens are added to avoid fractional token issues.
        """
        now = time.monotonic()
        elapsed = now - self.timestamp
        # Use math.floor and a small epsilon to avoid floating-point errors
        epsilon = 1e-9
        added_tokens = math.floor((elapsed + epsilon) * self.fill_rate)
        # Debug: print elapsed and tokens to trace behavior
        print(f"[DEBUG] Elapsed: {elapsed:.4f}s, Added tokens: {added_tokens}, Before: {self.tokens:.4f}")
        if added_tokens > 0:
            self.tokens = min(self.capacity, self.tokens + added_tokens)
            self.timestamp += added_tokens / self.fill_rate
            print(f"[DEBUG] After refill: {self.tokens:.4f}, Timestamp: {self.timestamp:.4f}")

    def allow_request(self, tokens=1):
        """
        Attempt to consume 'tokens' tokens from the bucket.
        Returns True if allowed, False otherwise.
        """
        self._add_new_tokens()
        print(f"[DEBUG] Allow request? Tokens needed: {tokens}, Available: {self.tokens:.4f}")
        if self.tokens >= tokens:
            self.tokens -= tokens
            print(f"[DEBUG] Request allowed. Tokens left: {self.tokens:.4f}")
            return True
        print(f"[DEBUG] Request denied. Tokens left: {self.tokens:.4f}")
        return False

# ------------------- TESTS -------------------
# These tests use time.sleep to simulate passage of time.
# In production, you would want to mock time for deterministic tests.

def test_token_bucket_basic():
    # Bucket with capacity 5, fill rate 1 token/sec
    bucket = TokenBucket(capacity=5, fill_rate=1)
    # Should allow 5 immediate requests
    for _ in range(5):
        assert bucket.allow_request() == True
    # 6th request should be denied
    assert bucket.allow_request() == False
    # Wait 1 second for 1 token to refill
    time.sleep(1.1)
    assert bucket.allow_request() == True
    # Should be empty again
    assert bucket.allow_request() == False

def test_token_bucket_burst():
    bucket = TokenBucket(capacity=3, fill_rate=2)  # 2 tokens/sec
    # Use all tokens
    for _ in range(3):
        assert bucket.allow_request() == True
    assert bucket.allow_request() == False
    # Wait 0.45s (should NOT refill 1 token)
    time.sleep(0.45)
    print("[TEST] Slept 0.45s")
    assert bucket.allow_request() == False  # Not enough for 1 token yet
    # Wait another 0.1s (total 0.55s, should refill 1 token)
    time.sleep(0.1)
    print("[TEST] Slept 0.1s more")
    assert bucket.allow_request() == True   # Now enough for 1 token
    # Wait 2s (should refill to max capacity)
    time.sleep(2)
    print("[TEST] Slept 2s")
    for _ in range(3):
        assert bucket.allow_request() == True
    assert bucket.allow_request() == False

def test_token_bucket_multi_token():
    bucket = TokenBucket(capacity=10, fill_rate=5)  # 5 tokens/sec
    # Use 7 tokens at once
    assert bucket.allow_request(tokens=7) == True
    assert bucket.allow_request(tokens=4) == False  # Only 3 left
    assert bucket.allow_request(tokens=3) == True
    assert bucket.allow_request(tokens=1) == False  # Empty
    # Wait 1 second (should refill 5 tokens)
    time.sleep(1.1)
    assert bucket.allow_request(tokens=5) == True
    assert bucket.allow_request(tokens=1) == False

if __name__ == "__main__":
    test_token_bucket_basic()
    test_token_bucket_burst()
    test_token_bucket_multi_token()
    print("All tests passed.")
