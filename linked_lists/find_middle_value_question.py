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


def find_middle_node_slow_fast_technique(head: ListNode) -> ListNode:
    pass

if __name__ == '__main__':
    head = ListNode(0, ListNode(1, ListNode(2, ListNode(3, ListNode(4)))))
    expected = 2
    result = find_middle_node_slow_fast_technique(head)
    print(f"list={head}, expected={expected}, result={result}")
    assert result == expected, f"Expected {expected}, but got {result}"

    head = ListNode(0, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))))
    expected = 3
    result = find_middle_node_slow_fast_technique(head)
    print(f"list={head}, expected={expected}, result={result}")
    assert result == expected, f"Expected {expected}, but got {result}"

    head = ListNode(0, ListNode(1))
    expected = 1
    result = find_middle_node_slow_fast_technique(head)
    print(f"list={head}, expected={expected}, result={result}")
    assert result == expected, f"Expected {expected}, but got {result}"