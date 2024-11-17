class Solution:
    def pushZerosToEnd(self, arr):
        n = len(arr)
        count = 0  # Count of non-zero elements
        
        # Traverse the array. If element encountered is non-zero, then
        # replace the element at index 'count' with this element
        for i in range(n):
            if arr[i] != 0:
                arr[count] = arr[i]
                count += 1
        
        # Now all non-zero elements have been shifted to the front and
        # 'count' is set as the index of the first 0. Make all elements
        # from count to end as 0.
        while count < n:
            arr[count] = 0
            count += 1

# Example usage:
arr = [0, 1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9]
solution = Solution()
solution.pushZerosToEnd(arr)
print("Array after pushing zeros to the end:", arr)
