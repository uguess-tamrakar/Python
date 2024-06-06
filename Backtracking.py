from typing import List

digitToChars = {
    '1': '',
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz',
    '0': '',
}
res = []
def letterCombinations(digits: str) -> List[str]:
    if len(digits) == 0: return []
    findCombinationsRecursive(digits, '')
    return res

def findCombinationsRecursive(digits: str, combination: str):
    if (len(digits) == len(combination)):
        res.append(combination)
        return
    chars = digitToChars[digits[len(combination)]]
    for char in chars:
        combination += char
        findCombinationsRecursive(digits, combination)
        combination = combination.rstrip(char)