from typing import List, Optional
from DataStructures import ListNode


class Solution:
    def lowestCommonAncestor(self, root, v1, v2):
        if root is None:
            return -1
        elif root.left is not None and v1 < root.info and v2 < root.info:
            return self.lowestCommonAncestor(root.left, v1, v2)
        elif root.right is not None and v1 > root.info and v2 > root.info:
            return self.lowestCommonAncestor(root.right, v1, v2)
        return root.info

    def sherlockAndAnagrams(self, s):
        refs = {}
        total = 0
        for start in range(len(s)):
            for length in range(1, len(s) - start + 1):
                sub = "".join(sorted(s[start : start + length]))
                if refs.__contains__(sub):
                    total += refs[sub]
                    refs[sub] += 1
                else:
                    refs[sub] = 1
        return total

    def containsDuplicate(self, nums: List[int]) -> bool:
        temp = set()
        for num in nums:
            if num in temp:
                return True
            else:
                temp.add(num)
        return False

    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        result = ListNode(0)
        curr = result
        carry = 0

        while l1 != None or l2 != None or carry != 0:
            l1Val = l1.val if l1 else 0
            l2Val = l2.val if l2 else 0
            columnSum = l1Val + l2Val + carry
            carry = columnSum // 10
            newNode = ListNode(columnSum % 10)
            curr.next = newNode
            curr = newNode
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return result.next
