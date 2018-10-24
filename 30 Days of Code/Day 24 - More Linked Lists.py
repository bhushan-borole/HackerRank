# https://www.hackerrank.com/challenges/30-linked-list-deletion/problem

def removeDuplicates(self,head):
    d = set()
    if head:
        while head:
            d.add(head.data)
            head = head.next
    t = None
    for x in sorted(d):
        t = mylist.insert(t, x)
    return t