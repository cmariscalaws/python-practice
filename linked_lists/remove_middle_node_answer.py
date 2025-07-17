class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
    
    def __str__(self):
        result = []
        current = self
        while current:
            result.append(str(current.val))
            current = current.next
        return ' -> '.join(result)

    def __eq__(self, other):
        if not isinstance(other, ListNode):
            return False

        current_self = self
        current_other = other

        while current_self and current_other:
            if current_self.val != current_other.val:
                return False
            current_self = current_self.next
            current_other = current_other.next

        # Make sure both lists are fully traversed (same length)
        return current_self is None and current_other is None


def remove_middle_node_slow_fast_technique(head: ListNode) -> ListNode:
    if not head or not head.next:
        return None

    # Use slow and fast pointer technique to find middle node
    # Fast moves twice as fast as slow
    slow = head
    fast = head
    prev = None

    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next

    if prev: # if the middle node is not the head
        prev.next = slow.next
    else:
        head = slow.next

    return head

def remove_middle_node(head: ListNode) -> ListNode:
    # Handle edge cases
    if not head or not head.next:
        return None

    # count nodes to find middle
    length = 0
    current = head
    while current:
        length += 1
        current = current.next

    # Calculate the position of the node to remove
    # For length 5: 5//2 = 2 (remove index 2, which is the 3rd node)
    # For length 4: 4//2 = 2 (remove index 2, which is the 3rd node)
    # For length 2: 2//2 = 1 (remove index 1, which is the 2nd node)
    middle = length // 2

    dummy = ListNode(-1, head)
    current = dummy

    # Move to the node before the one we want to remove
    for _ in range(middle):
        current = current.next

    # Remove the node
    current.next = current.next.next

    return dummy.next


if __name__ == '__main__':
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    expectedResult = ListNode(1, ListNode(2, ListNode(4, ListNode(5))))
    new_head = remove_middle_node_slow_fast_technique(head)
    print("result:")
    print(new_head)
    print("expected:")
    print(expectedResult)
    assert new_head == expectedResult, f"Expected {expectedResult}, but got {new_head}"

    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    expectedResult = ListNode(1, ListNode(2, ListNode(4)))
    new_head = remove_middle_node_slow_fast_technique(head)
    print("result:")
    print(new_head)
    print("expected:")
    print(expectedResult)
    assert new_head == expectedResult, f"Expected {expectedResult}, but got {new_head}"

    head = ListNode(1, ListNode(2))
    expectedResult = ListNode(1)
    new_head = remove_middle_node_slow_fast_technique(head)
    print("result:")
    print(new_head)
    print("expected:")
    print(expectedResult)
    assert new_head == expectedResult, f"Expected {expectedResult}, but got {new_head}"