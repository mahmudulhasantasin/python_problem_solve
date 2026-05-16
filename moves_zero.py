def moveZeroes(nums):
    insert_pos = 0

    # Step 1: Move all non-zero elements forward
    for num in nums:
        if num != 0:
            nums[insert_pos] = num
            insert_pos += 1

    # Step 2: Fill remaining positions with zeros
    while insert_pos < len(nums):
        nums[insert_pos] = 0
        insert_pos += 1