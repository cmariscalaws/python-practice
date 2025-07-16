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


def remove_kth_last_node(head: ListNode, k: int) -> ListNode:

    if k < 1:
        return head

    # create a dummy head
    dummyHead = ListNode(-1, head)

    # initialize two pointers, leader and trailer
    leader = trailer = dummyHead

    # separate the leader and trailer by k steps
    for _ in range(k):
        leader = leader.next
        # k is greater than size then return original list
        if not leader:
            return head

    # iterate until end of list where leader no longer has a next node
    while leader.next:
        # move both leader and trailer until end of list
        leader = leader.next
        trailer = trailer.next

    # replace trailer's next (removing kth element from end of list)
    trailer.next = trailer.next.next

    return dummyHead.next

if __name__ == '__main__':
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    expectedResult = ListNode(1, ListNode(2, ListNode(3, ListNode(5))))
    new_head = remove_kth_last_node(head, 2)
    print("result:")
    print(new_head)
    print("expected:")
    print(expectedResult)
    assert new_head == expectedResult, f"Expected {expectedResult}, but got {new_head}"

    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    expectedResult = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    new_head = remove_kth_last_node(head, 0)
    print("result:")
    print(new_head)
    print("expected:")
    print(expectedResult)
    assert new_head == expectedResult, f"Expected {expectedResult}, but got {new_head}"

    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    expectedResult = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    new_head = remove_kth_last_node(head, 6)
    print("result:")
    print(new_head)
    print("expected:")
    print(expectedResult)
    assert new_head == expectedResult, f"Expected {expectedResult}, but got {new_head}"

    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    expectedResult = ListNode(2, ListNode(3, ListNode(4, ListNode(5))))
    new_head = remove_kth_last_node(head, 5)
    print("result:")
    print(new_head)
    print("expected:")
    print(expectedResult)
    assert new_head == expectedResult, f"Expected {expectedResult}, but got {new_head}"