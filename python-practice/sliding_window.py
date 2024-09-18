# Author: @Tiffany Wang
# Date: 09/18/2024
# Objective: Prep for Tiktok Site Reliability Engineer (USDS) interview
# with Hyunil Yoo at 2:30 pm.


def max_sum_subarray(arr, k):
    if len(arr) < k:
        print("Invalid input: Array size is smaller than the window size.")
        return None

    # Initial the window and max result
    max_sum = 0
    window_sum = 0

    # Calculate the sum of first window of size k
    for i in range(k):
        window_sum += arr[i]

    max_sum = window_sum

    # Slide window
    for i in range(k, len(arr)):
        # substracting the element that is left behind
        # and adding the next element in the window.
        window_sum = window_sum - arr[i-k] + arr[i]
        max_sum = max(window_sum, max_sum)

    return max_sum


# test by print out
test_arr = [2, 1, 34, 5, 1, 4, 5, 1902]
k = 2
print(max_sum_subarray(test_arr, k))
