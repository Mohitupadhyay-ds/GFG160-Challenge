class Solution:
    # Function to find the smallest positive number missing from the array.
    def missingNumber(self, arr):
        n = len(arr)
        
        # Step 1: Place each positive integer at its correct index if possible
        for i in range(n):
            while 1 <= arr[i] <= n and arr[arr[i] - 1] != arr[i]:
                arr[arr[i] - 1], arr[i] = arr[i], arr[arr[i] - 1]
        
        # Step 2: Identify the first missing positive integer
        for i in range(n):
            if arr[i] != i + 1:
                return i + 1
        
        # If all numbers from 1 to n are present, return n + 1
        return n + 1

# Example Usage
solution = Solution()

# Test cases
test_cases = [
    [2, -3, 4, 1, 1, 7],   # Output: 3
    [1, 2, 3, 4],          # Output: 5
    [-1, -2, -3],          # Output: 1
    [0, 0, 2, 2, 3, 1],    # Output: 4
    [10, 3, 5, -1, 1],     # Output: 2
]

for i, test in enumerate(test_cases, 1):
    print(f"Test case {i}: {solution.missingNumber(test)}")