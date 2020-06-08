class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        nums = ''
        for digit in digits:
            nums += str(digit)
        nums = int(nums)
        nums += 1
        digitsOne = []
        for num in str(nums):
            digitsOne.append(int(num))
        return digitsOne
