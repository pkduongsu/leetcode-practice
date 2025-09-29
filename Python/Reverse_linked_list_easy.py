#Iterative:
#Time: O(n) where n is the maximum length of the linked list
#Space: O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #Input: beginning of a singly linkedin list  - head
        #Output: the new begininng of the list, which other nodes points to the reverse of original linked list
        #Ex: 1 -> 2 -> 3 -> 4 => 4 -> 3 -> 2 -> 1
        current, prev = head, None 

        while current: #if there are no other nodes, next points to None => we know its the end of the list
            temp = current.next
            current.next = prev
            prev = current  #advance the pointers to the next node
            current = temp

        return prev #as the final node current will be none, signaling end of linked list, while prev is the new beginning
        
        
#Recursive approach:
#Time: O(n)
#Space: O(n) - due to recursion call stack (depth n in worst case)
def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #Input: beginning of a singly linkedin list  - head
        #Output: the new begininng of the list, which other nodes points to the reverse of original linked list
        #Ex: 1 -> 2 -> 3 -> 4 => 4 -> 3 -> 2 -> 1
        
        #Recursive approach:
        if not head:
            return None

        newHead = head

        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head

        head.next = None

        return newHead


