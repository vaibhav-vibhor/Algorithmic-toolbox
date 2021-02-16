def max_pairwise_product(nums):
    n = len(nums)
    p = 0
    p_index = 0
    q = 0
    for i in range(n):
        if nums[i] > p:
            p = nums[i]
            p_index = i

    for j in range(n):
        if nums[j] > q and j != p_index:
            q = nums[j]

    return p*q


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
