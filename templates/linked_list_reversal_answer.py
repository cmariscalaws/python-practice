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
    # initialize previous pointer to None since in single LinkedList there is no previous Node at head of list
    # (1 is the head) None <- 1 -> 2 -> 3 -> 4 -> 5
    prev = None
    # pointer to current node
    # pointer to start of list
    current = head

    # loop until current node is None
    # iterate until current is set to None indicating end of the list
    while current:
        # start the swap: get the pointer to the next node from current node
        # store the next node in a temp variable
        next = current.next
        # complete the swap: reversing the pointers using previous as next pointer
        # set the current node's next to previous node'
        current.next = prev

        # set the previous node to current node for next iteration swap
        # set previous node to current node
        prev = current

        # set current node to the next node for next iteration swap
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