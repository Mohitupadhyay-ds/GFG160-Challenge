class Solution:
    def getMinDiff(self, k, arr):
        n = len(arr)
        
        # Edge case: If the array contains only one element, there's no difference
        if n == 1:
            return 0
        
        # Sort the array
        arr.sort()
        
        # Initialize the result as the difference between the max and min heights
        result = arr[-1] - arr[0]
        
        # Loop through the array and check for all possible adjustments
        for i in range(1, n):
            # The possible new minimum and maximum after adding or subtracting k
            min_height = min(arr[0] + k, arr[i] - k)
            max_height = max(arr[-1] - k, arr[i-1] + k)
            
            # Update the result with the minimum difference
            result = min(result, max_height - min_height)
        
        return result

