class Solution:
    def addBinary(self, s1, s2):
        # Remove leading zeros and handle empty strings
        s1 = s1.lstrip('0') or '0'
        s2 = s2.lstrip('0') or '0'

        # Convert binary strings to integers, add them, then convert back to binary
        sum_decimal = int(s1, 2) + int(s2, 2)
        result = bin(sum_decimal)[2:]  # bin(x) gives a binary string prefixed with '0b'

        return result


# Testing with multiple test cases
solution = Solution()
test_cases = [
    ("1101", "111"),      # Expected output: "10100"
    ("0", "0"),           # Expected output: "0"
    ("1010", "0101"),     # Expected output: "1111"
    ("000110", "111"),    # Expected output: "1101"
    ("1111", "1"),        # Expected output: "10000"
    ("000", "000"),       # Expected output: "0" (edge case with all leading zeros)
]

for s1, s2 in test_cases:
    print(f"s1: {s1}, s2: {s2} -> Output: {solution.addBinary(s1, s2)}")
