# def contracting(l):
#     # Check each adjacent pair of differences
#     for i in range(len(l) - 2):
#         # Calculate the absolute difference of the current pair
#         diff1 = abs(l[i] - l[i+1])
        
#         # Calculate the absolute difference of the next adjacent pair
#         diff2 = abs(l[i+1] - l[i+2])
        
#         # If the next difference is NOT strictly smaller, it breaks the rule
#         if diff2 >= diff1:
#             return False
            
#     # If all pairs strictly decrease, return True
#     return True
# print(contracting([9,2,7,3,1]))  # Output: true
# print(contracting([10,7,4,1]))  # Output: false
def counthv(l):
    # Initialize counters for hills (hc) and valleys (vc)
    hc = 0
    vc = 0
    
    # Iterate through the list, skipping the first and last elements
    for i in range(1, len(l) - 1):
        # A hill is strictly greater than both its left and right neighbors
        if l[i] > l[i-1] and l[i] > l[i+1]:
            hc += 1
            
        # A valley is strictly less than both its left and right neighbors
        elif l[i] < l[i-1] and l[i] < l[i+1]:
            vc += 1
            
    # Return the results as a list containing [hill_count, valley_count]
    return [hc, vc]

# Test cases from the assignment sheet
print(counthv([1, 2, 1, 2, 3, 2, 1]))  # Expected output: [2, 1]
print(counthv([1, 2, 3, 1]))           # Expected output: [1, 0]
print(counthv([3, 1, 2, 3]))           # Expected output: [0, 1]