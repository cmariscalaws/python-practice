from templates.utils import ListNode

# Function: find_middle_node_slow_fast_technique
# Purpose: Returns the value of the middle node in a singly linked list using the slow/fast pointer technique.
# Parameters:
#   head (ListNode): The head node of the singly linked list.
# Returns:
#   int: The value of the middle node.
def find_middle_node(head: ListNode) -> int:
    # Initialize two pointers, both starting at the head.
    slow = fast = head
    # Move 'fast' two steps and 'slow' one step until 'fast' reaches the end.
    # Continue looping while 'fast' and 'fast.next' are not None.
    # This ensures 'fast' can move two steps ahead safely.
    while fast and fast.next:
        slow = slow.next         # Move slow pointer one step.
        fast = fast.next.next    # Move fast pointer two steps.
    # When fast reaches the end, slow will be at the middle node.
    return slow.val

if __name__ == '__main__':
    head = ListNode(0, ListNode(1, ListNode(2, ListNode(3, ListNode(4)))))
    expected = 2
    result = find_middle_node(head)
    print(f"list={head}, expected={expected}, result={result}")
    assert result == expected, f"Expected {expected}, but got {result}"

    head = ListNode(0, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))))
    expected = 3
    result = find_middle_node(head)
    print(f"list={head}, expected={expected}, result={result}")
    assert result == expected, f"Expected {expected}, but got {result}"

    head = ListNode(0, ListNode(1))
    expected = 1
    result = find_middle_node(head)
    print(f"list={head}, expected={expected}, result={result}")
    assert result == expected, f"Expected {expected}, but got {result}"