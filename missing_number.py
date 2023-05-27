def find_missing_number(array):
    n = 100  # Maximum number in the array
    total_sum = (n * (n + 1)) // 2
    array_sum = sum(array)
    missing_number = total_sum - array_sum
    return missing_number


# Example usage
integer_array = [1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 100]  # Array with one missing number
missing_number = find_missing_number(integer_array)
print("Missing number:", missing_number)
