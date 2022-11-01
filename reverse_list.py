def reverse_list(head):
    prev = None
    curr = head
    while curr != None:
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp
    return prev


def reserve_list_by_stack(head):
    if head == None:
        return head
    stack = []

    curr = head
    while curr.next != None:
        stack.append(curr)
        curr = curr.next
    # 역전 후 첫 노드를 임시 저장하고 반환해야한다
    first = curr

    while stack:
        curr.next = stack.pop()
        curr = curr.next
    curr.next = None
    return first
