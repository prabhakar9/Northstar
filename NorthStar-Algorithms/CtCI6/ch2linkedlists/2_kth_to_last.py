from CtCI6.ch2linkedlists.LinkedList import LinkedList


def kth_to_last(ll, k):
    current = ll.head

    count = 0

    while current:
        count += 1
        if count < k:
            current = current.next
        else:
            ll.head = current.next
            return ll


if __name__ == "__main__":
    ll = LinkedList()
    ll.generate(10, 0 ,99)
    print(ll)
    ll = kth_to_last(ll, 3)
    print(ll)