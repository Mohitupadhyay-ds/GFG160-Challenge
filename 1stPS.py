class Solution:
 def find_second_largest(self ,arr): 
    if len(arr) < 2: 
        return -1 
    
    first_largest = second_largest = float('-inf') 
    
    for num in arr: 
        if num > first_largest: 
            second_largest = first_largest 
            first_largest = num 
            
        elif num > second_largest and num != first_largest: 
            second_largest = num 

    return second_largest if second_largest != float('-inf') else -1
    
#check usage
solution = Solution()
arr = [10, 5, 4, 3, 8] 
result = solution.find_second_largest(arr) 
print("Second largest element is:", result)