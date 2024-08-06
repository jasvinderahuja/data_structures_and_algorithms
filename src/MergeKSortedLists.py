## 23. Merge k Sorted Lists
## https://leetcode.com/problems/merge-k-sorted-lists/description/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        import heapq
        h = []
        for lst in lists:
            while lst:
                ## print(lst.val)
                heapq.heappush(h, lst.val)
                lst = lst.next
        
        res = ListNode(0)
        return_res = res

        while h:
            res.next = ListNode()
            res = res.next
            res.val = heapq.heappop(h)
        
        return return_res.next

	