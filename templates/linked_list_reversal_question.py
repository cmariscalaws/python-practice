from utils import ListNode

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