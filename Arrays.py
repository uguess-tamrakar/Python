import sys


class Arrays:
    def maxProduct(inputArray):
        maxProduct = float('-inf')
        for i in range(1, len(inputArray)):
            current = inputArray[i] + inputArray[i-1]
            maxProduct = max(maxProduct, current)
        return maxProduct

    def almostIncreasingSequence(sequence):
        removed = 0
        lastMax = sequence[0]
        for x in range(1, len(sequence)):
            if (sequence[x-1] > sequence[x] and sequence[x] < sequence[x+1]) or (sequence[x-1] < sequence[x] and sequence[x] > sequence[x+1]):
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