from CtCI6.ch2linkedlists.LinkedList import LinkedList


def delete_middle_node(ll):
    slow_ptr = fast_ptr = ll.head
    if fast_ptr.next is None:
        return ll
    elif fast_ptr.next.next is None:
        return ll
    else:
        fast_ptr = fast_ptr.next.next

    while fast_ptr.next:
        if fast_ptr.next:
            if fast_ptr.next.next:
                fast_ptr = fast_ptr.next.next
                slow_ptr = slow_ptr.next
            else:
                slow_ptr.next = slow_ptr.next.next
                return ll
        else:
            slow_ptr.next = slow_ptr.next.next
            return ll
    slow_ptr.next = slow_ptr.next.next
    return ll


if __name__ == "__main__":
    ll = LinkedList()
    ll.generate(7, 0, 99)
    print(ll)
    delete_middle_node(ll)
    print(ll)