from math import inf
import sys


class Arrays:
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
