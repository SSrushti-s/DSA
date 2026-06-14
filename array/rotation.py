# Left rotate an array by d elements
def left_rotate(arr, d):
    n = len(arr)
    d = d % n  # Handle cases where d >= n
    return arr[d:] + arr[:d]

# Optimized approach using reversal algorithm
def left_rotate_reversal(arr, d):
    n = len(arr)
    d = d % n  # Handle cases where d >= n

    # Helper function to reverse a portion of the array
    def reverse(sub_arr, start, end):
        while start < end:
            sub_arr[start], sub_arr[end] = sub_arr[end], sub_arr[start]
            start += 1
            end -= 1

    # Step 1: Reverse the first d elements
    reverse(arr, 0, d - 1)
    # Step 2: Reverse the remaining n-d elements
    reverse(arr, d, n - 1)
    # Step 3: Reverse the entire array
    reverse(arr, 0, n - 1)

    return arr

# Example usage
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    d = 2
    print("Original array:", arr)
    print("Left rotated array (simple):", left_rotate(arr.copy(), d))
    print("Left rotated array (reversal):", left_rotate_reversal(arr.copy(), d))

# Right rotate an array by d elements
def right_rotate(arr, d):
    n = len(arr)
    d = d % n  # Handle cases where d >= n
    return arr[-d:] + arr[:-d]

# Optimized approach using reversal algorithm for right rotation
def right_rotate_reversal(arr, d):
    n = len(arr)
    d = d % n  # Handle cases where d >= n

    # Helper function to reverse a portion of the array
    def reverse(sub_arr, start, end):
        while start < end:
            sub_arr[start], sub_arr[end] = sub_arr[end], sub_arr[start]
            start += 1
            end -= 1

    # Step 1: Reverse the last d elements
    reverse(arr, n - d, n - 1)
    # Step 2: Reverse the first n-d elements
    reverse(arr, 0, n - d - 1)
    # Step 3: Reverse the entire array
    reverse(arr, 0, n - 1)

    return arr
# Example usage for right rotation
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    d = 2
    print("Original array:", arr)
    print("Right rotated array (simple):", right_rotate(arr.copy(), d))
    print("Right rotated array (reversal):", right_rotate_reversal(arr.copy(), d))