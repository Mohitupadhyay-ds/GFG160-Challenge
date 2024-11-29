class Solution:
    # Function to find the maximum product subarray
    def maxProduct(self, arr):
        # Initialize variables
        max_so_far = arr[0]  # Stores the maximum product found so far
        max_ending_here = arr[0]  # Maximum product of the subarray ending at the current index
        min_ending_here = arr[0]  # Minimum product of the subarray ending at the current index

        # Traverse the array starting from the second element
        for i in range(1, len(arr)):
            # If current element is negative, swap max_ending_here and min_ending_here
            if arr[i] < 0:
                max_ending_here, min_ending_here = min_ending_here, max_ending_here

            # Update max_ending_here and min_ending_here
            max_ending_here = max(arr[i], max_ending_here * arr[i])
            min_ending_here = min(arr[i], min_ending_here * arr[i])

            # Update max_so_far to store the result
            max_so_far = max(max_so_far, max_ending_here)

        return max_so_far

# Example usage
sol = Solution()
arr = [-2, 6, -3, -10, 0, 2]
print(sol.maxProduct(arr))  # Output: 180
