class Solution:
    def reverseArray(self, arr):
        left = 0
        right = len(arr) - 1

        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

# Example usage:
arr = [2 , 8 , 0 , 10 , 3]
solution = Solution()
solution.reverseArray(arr)
print("Reversed array:", arr)
