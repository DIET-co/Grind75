def two_sum(nums, target):
    """
    Returns indices of two numbers in the list that add up to the target sum.

    :param nums: List of integers
    :param target: Target sum
    :return: Indices of two numbers that add up to the target sum
    """
    num_dict = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            return [num_dict[complement], i]
        num_dict[num] = i
    return None

def main():
    # Get user input for the list of numbers
    nums = input("Enter a list of numbers separated by spaces: ")
    nums = [int(x) for x in nums.split()]

    # Get user input for the target sum
    target = int(input("Enter the target sum: "))

    # Call the two_sum function
    result = two_sum(nums, target)

    # Print the result
    if result:
        print("Indices of two numbers that add up to the target sum:", result)
    else:
        print("No two numbers add up to the target sum.")

if __name__ == "__main__":
    main()