# collection_examples/dequeue_example.py

from collections import deque

def demo_deque_operations():
    d = deque()
    print(f"initialized: {d}")
    d.append('a')        # Add to the right
    print(f"added 'a' to the right: {d}")
    d.appendleft('b')    # Add to the left
    print(f"added 'b' to the left: {d}")
    d.append('c')
    print(f"added 'c' to the right: {d}")
    right = d.pop()      # Remove from the right
    print(f"popped from the right: {d}")
    left = d.popleft()   # Remove from the left
    print(f"popped from the left: {d}")
    return list(d), right, left

def test_demo_deque_operations():
    result, right, left = demo_deque_operations()
    print(f"result: {result}, right: {right}, left: {left}")
    assert result == ['a'], f"Expected ['a'], got {result}"
    assert right == 'c', f"Expected 'c', got {right}"
    assert left == 'b', f"Expected 'b', got {left}"
    print("All tests passed.")

if __name__ == "__main__":
    test_demo_deque_operations()