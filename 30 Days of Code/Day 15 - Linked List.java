// https://www.hackerrank.com/challenges/30-linked-list/problem

public static  Node insert(Node head,int data) {
    if(head == null)
        head = new Node(data);
    else if(head.next == null)
        head.next = new Node(data);
    else
        insert(head.next, data);
    return head;
}