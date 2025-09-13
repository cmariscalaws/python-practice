from utils import ListNode

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