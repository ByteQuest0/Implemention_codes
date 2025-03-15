def lengthOfLIS(nums):
    n = len(nums)
    dp = [1] * n  # Initialize DP array

    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)
