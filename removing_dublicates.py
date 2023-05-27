def remove_duplicates(nums):
    if len(nums) == 0:
        return 0

    i = 1
    for j in range(1, len(nums)):
        if nums[j] != nums[i-1]:
            nums[i] = nums[j]
            i += 1

    return i

# Example usage
array = [1, 2, 2, 3, 4, 4, 4, 5, 6, 6]
new_length = remove_duplicates(array)
print("Array without duplicates:", array[:new_length])