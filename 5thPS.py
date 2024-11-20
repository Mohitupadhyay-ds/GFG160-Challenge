class Solution:
    def nextPermutation(self, arr):
        n = len(arr)
        
        # Step 1: Find the first decreasing element from the end
        i = n - 2
        while i >= 0 and arr[i] >= arr[i + 1]:
            i -= 1
        
        if i >= 0:
            # Step 2: Find the element just larger than arr[i]
            j = n - 1
            while arr[j] <= arr[i]:
                j -= 1
            
            # Step 3: Swap elements at i and j
            arr[i], arr[j] = arr[j], arr[i]
        
        # Step 4: Reverse the elements from i + 1 to the end of the array
        self.reverseArray(arr, i + 1, n - 1)
    
    def reverseArray(self, arr, start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

# Example usage:
arr = [2, 4, 1, 7, 5, 0]
solution = Solution()
solution.nextPermutation(arr)
print("Next permutation:", arr)
