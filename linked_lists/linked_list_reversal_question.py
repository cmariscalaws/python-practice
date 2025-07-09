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

def linked_list_reversal(head: ListNode) -> ListNode:
    return head

if __name__ == '__main__':
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    expectedResult = ListNode(5, ListNode(4, ListNode(3, ListNode(2, ListNode(1)))))
    head = linked_list_reversal(head)
    print("result:")
    print(head)
    print("expected:")
    print(expectedResult)
    assert head == expectedResult, f"Expected {expectedResult}, but got {head}"