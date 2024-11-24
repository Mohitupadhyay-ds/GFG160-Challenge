class Solution:
# Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self, arr):
        # Initialize variables
        max_so_far = float('-inf')  # To keep track of the overall maximum sum
        max_ending_here = 0  # To keep track of the current subarray sum

        for num in arr:
            # Update the running sum of the current subarray
            max_ending_here += num

            # Update the overall maximum sum if the current sum is greater
            max_so_far = max(max_so_far, max_ending_here)

            # Reset the running sum to 0 if it becomes negative
            if max_ending_here < 0:
                max_ending_here = 0

        return max_so_far

# Test cases
test_cases = [
    ([2, 3, -8, 7, -1, 2, 3], 11),  # Mixed numbers
    ([1, 2, 3, 4], 10),             # All positive numbers
    ([-1, -2, -3, -4], -1),         # All negative numbers
    ([5], 5),                       # Single positive element
    ([-5], -5),                     # Single negative element
    ([3, -2, 5, -1], 6),            # Mix with overlapping subarray
    ([-2, -3, 4, -1, -2, 1, 5, -3], 7),  # Classic test case
]

# Run tests
solution = Solution()
for i, (arr, expected) in enumerate(test_cases):
    result = solution.maxSubArraySum(arr)
    assert result == expected, f"Test case {i + 1} failed: got {result}, expected {expected}"
print("All test cases passed!")




























