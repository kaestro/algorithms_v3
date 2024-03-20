from typing import List

def wiggle_sort(nums):
    # Count the frequency of each number
    count = [0] * 5001
    for num in nums:
        count[num] += 1

    # Generate the sorted array
    sorted_nums = []
    for num, freq in enumerate(count):
        sorted_nums.extend([num] * freq)

    # Wiggle sort
    mid = len(nums[::2]) - 1
    nums[::2], nums[1::2] = sorted_nums[mid::-1], sorted_nums[len(nums)-1:mid:-1]
    return nums