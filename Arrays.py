from math import inf
import sys
from typing import List

class Arrays:
    def canJump(nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        lastIdx = n - 1
        for idx in range(lastIdx - 1, -1, -1):
            if lastIdx <= idx + nums[idx]: 
                lastIdx = idx
        return lastIdx <= 0


    def peakElement(self, arr, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        for idx in range(arr):
            if (
                (idx == 0 and arr[idx] >= arr[idx + 1])
                or (idx == n - 1 and arr[idx] >= arr[idx - 1])
                or (
                    idx > 0
                    and idx < n - 1
                    and arr[idx - 1] <= arr[idx]
                    and arr[idx] >= arr[idx + 1]
                )
            ):
                return 1

        return 0

    def minJumps(arr, n):
        if n <= 1:
            return 0
        if arr[0] == 0:
            return -1

        max_jump = arr[0]
        steps = arr[0]
        jumps = 1

        for idx in range(1, n):
            if idx == n - 1:
                return jumps

            max_jump = max(max_jump, idx + arr[idx])
            steps -= 1

            if steps == 0:
                jumps += 1
                if idx >= max_jump:
                    return -1
                steps = max_jump - idx
        return -1

    def maxProduct(inputArray):
        maxProduct = float("-inf")
        for i in range(1, len(inputArray)):
            current = inputArray[i] + inputArray[i - 1]
            maxProduct = max(maxProduct, current)
        return maxProduct
    
    def maxProductSubarray(nums):
        n = len(nums)
        prefix = 1
        suffix = 1
        maxProduct = -inf
        for i in range(n):
            if prefix == 0:
                prefix = 1
            if suffix == 0:
                suffix = 1
            prefix *= nums[i]
            suffix *= nums[n - i - 1]
            maxProduct = max(maxProduct, max(prefix, suffix))
        return maxProduct

    def almostIncreasingSequence(sequence):
        removed = 0
        lastMax = sequence[0]
        for x in range(1, len(sequence)):
            if (sequence[x - 1] > sequence[x] and sequence[x] < sequence[x + 1]) or (
                sequence[x - 1] < sequence[x] and sequence[x] > sequence[x + 1]
            ):
                removed += 1
                lastMax = sequence[x]
            else:
                if sequence[x] <= lastMax:
                    removed += 1
                    if removed > 1:
                        return False
                else:
                    lastMax = sequence[x]
        return True
