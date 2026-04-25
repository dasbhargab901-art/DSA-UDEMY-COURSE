# Fibonacci using Tabulation (Bottom-Up)
# Calculation: F(n) = F(n-1) + F(n-2)
# Time Complexity: O(n)
# Space Complexity: O(n)


def fib_tabulation(n):
    """
    Calculates the nth Fibonacci number starting from F(0) = 0, F(1) = 1.
    This is an iterative Bottom-Up approach.
    """
    # Handle base cases for small n
    if n <= 0:
        return 0
    if n == 1:
        return 1

    # Create the DP table up to n
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1

    # Build the table iteratively
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


if __name__ == "__main__":
    n = 5
    print(f"Fibonacci number at position {n} is: {fib_tabulation(n)}")
    # Expected: F(0)=0, F(1)=1, F(2)=1, F(3)=2, F(4)=3, F(5)=5
