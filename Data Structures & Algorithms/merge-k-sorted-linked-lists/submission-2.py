# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        interval = 1

        while interval < len(lists):
            for i in range(0, len(lists) - interval, interval * 2):
                lists[i] = self.mergeTwoLists(lists[i], lists[i + interval])
            
            interval *= 2
        
        return lists[0]


    def mergeTwoLists(self,list1, list2):
        temp1 = list1
        temp2 = list2
        dummy = ListNode()
        pntr = dummy
        while temp1 and temp2:
            if temp1.val <= temp2.val:
                pntr.next = temp1
                temp1 = temp1.next
            else:
                pntr.next = temp2
                temp2 = temp2.next
            pntr = pntr.next
        
        pntr.next = temp1 if not temp2 else temp2

        return dummy.next
        
    
        
        