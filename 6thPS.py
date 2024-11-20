class Solution:
    def findMajority(self, arr):
        n = len(arr)
        if n == 0:
            return []
        
        # Step 1: Find potential candidates
        candidate1, candidate2, count1, count2 = None, None, 0, 0
        for num in arr:
            if candidate1 == num:
                count1 += 1
            elif candidate2 == num:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = num, 1
            elif count2 == 0:
                candidate2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1
        
        # Step 2: Verify the candidates
        count1, count2 = 0, 0
        for num in arr:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
        
        # Step 3: Collect the valid candidates
        result = []
        if count1 > n // 3:
            result.append(candidate1)
        if count2 > n // 3:
            result.append(candidate2)
        
        return sorted(result)

# Example usage:
arr = [1, 2, 3, 4, 5]
solution = Solution()
print("Majority elements:", solution.findMajority(arr))
