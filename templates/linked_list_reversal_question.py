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
    pass

if __name__ == '__main__':
    print("--- Test 1 ---")
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    expectedResult = ListNode(5, ListNode(4, ListNode(3, ListNode(2, ListNode(1)))))
    new_head = linked_list_reversal(head)
    print("result:")
    print(new_head)
    print("expected:")
    print(expectedResult)
    assert new_head == expectedResult, f"Expected {expectedResult}, but got {new_head}"

    print("--- Test 2 ---")
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
    expectedResult = ListNode(6, ListNode(5, ListNode(4, ListNode(3, ListNode(2, ListNode(1))))))
    new_head = linked_list_reversal(head)
    print("result:")
    print(new_head)
    print("expected:")
    print(expectedResult)
    assert new_head == expectedResult, f"Expected {expectedResult}, but got {new_head}"