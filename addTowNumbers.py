class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None


def addTwoNumbers(l1: Node, l2: Node) -> Node:
    st1 = []
    st2 = []

    l1_curr = l1
    l2_curr = l2

    while l1_curr != None:
        st1.append(l1_curr.val)
        l1_curr = l1_curr.next
    while l2_curr != None:
        st2.append(l2_curr.val)
        l2_curr = l2_curr.next
    carry = 0
    while st1 or st2:
        num1 = st1.pop() if st1 else 0
        num2 = st2.pop() if st2 else 0

        carry, num = divmod(num1+num2+carry, 10)

        node = Node(num)
        if head == None:
            head = node
        else:
            temp = head
            head = node
            node.next = temp
    if carry != 0:
        node = Node(carry)
        temp = head
        head = node
        node.next = temp
    return head
