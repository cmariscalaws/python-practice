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

def linked_list_reversal(head: ListNode) -> ListNode:
    # pointer to previous node
    prev = None
    # pointer to current node
    current = head

    # loop until current node is None
    while current:
        # store the next node in a temp variable
        next = current.next
        # set the current node's next to previous node'
        current.next = prev
        # set previous node to current node
        prev = current
        # set current node to next node
        current = next

    # return previous node which is now the head of the reversed linked list
    return prev

if __name__ == '__main__':
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    expectedResult = ListNode(5, ListNode(4, ListNode(3, ListNode(2, ListNode(1)))))
    new_head = linked_list_reversal(head)
    print("result:")
    print(new_head)
    print("expected:")
    print(expectedResult)
    assert new_head == expectedResult, f"Expected {expectedResult}, but got {new_head}"