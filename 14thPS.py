class Solution:
    def myAtoi(self, s):
        # Step 1: Trim leading and trailing whitespaces
        s = s.strip()
        if not s:
            return 0  # If string is empty after trimming

        # Step 2: Initialize variables
        sign = 1  # Default positive sign
        result = 0
        i = 0
        n = len(s)

        # Step 3: Check for the sign
        if s[i] == '-' or s[i] == '+':
            sign = -1 if s[i] == '-' else 1
            i += 1

        # Step 4: Process digits and build the number
        while i < n and s[i].isdigit():
            digit = int(s[i])  # Convert character to digit
            result = result * 10 + digit
            i += 1

            # Step 5: Handle overflow
            if result > 2**31 - 1:
                return (2**31 - 1) if sign == 1 else -2**31

        return result * sign

# Test cases
test_cases = [
    "42",               # Basic positive number
    "   -42",           # Leading spaces with negative number
    "4193 with words",  # Number followed by non-digits
    "words and 987",    # Invalid leading characters
    "-91283472332",     # Negative overflow
    "3.14159",          # Decimal input
    "",                 # Empty string
    "00000",            # Leading zeros
    "+123456",          # Positive number with explicit sign
]

solution = Solution()
for s in test_cases:
    print(f"Input: '{s}' -> Output: {solution.myAtoi(s)}")
