class Solution:
    def rotateArr(self, arr, d):
        n = len(arr)
        d = d % n  # To handle cases where d > n
        
        # Step 1: Reverse the first part
        self.reverseArray(arr, 0, d - 1)
        
        # Step 2: Reverse the second part
        self.reverseArray(arr, d, n - 1)
        
        # Step 3: Reverse the entire array
        self.reverseArray(arr, 0, n - 1)
    
    # Helper function to reverse a portion of the array
    def reverseArray(self, arr, start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

# Example usage:
arr = [1, 2, 3, 4, 5, 6, 7]
d = 3
solution = Solution()
solution.rotateArr(arr, d)
print("Array after rotating to the left by", d, "steps:", arr)
