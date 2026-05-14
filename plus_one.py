def plusOne(digits):
    n = len(digits)
    
    # Traverse from the end
    for i in range(n - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0  # carry over
    
    # If all digits were 9
    return [1] + [0] * n