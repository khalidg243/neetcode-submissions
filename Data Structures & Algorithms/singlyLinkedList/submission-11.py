class ListNode:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node


class LinkedList:
    
    def __init__(self):
        self.head= ListNode(-1)
        self.tail= self.head

    
    def get(self, index: int) -> int:
        temp= self.head.next
        i=0

        while temp:
            if i==index:
                return temp.val
            i += 1 
            temp = temp.next
        return -1

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next= self.head.next
        self.head.next=new_node
        if not new_node.next:
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        self.tail.next= ListNode(val)
        self.tail=self.tail.next

    def remove(self, index: int) -> bool:
        temp = self.head
        i=0

        while i<index and temp:
            temp=temp.next
            i+=1

        if temp and temp.next:
            if temp.next == self.tail:
                self.tail=temp
            temp.next = temp.next.next
            return True
        return False



    def getValues(self) -> List[int]:
        curr= self.head.next
        res = []
        while curr:
            res.append(curr.val)
            curr=curr.next
        return res

    