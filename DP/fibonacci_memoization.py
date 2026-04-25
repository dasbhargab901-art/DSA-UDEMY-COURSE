# Fibonacci using Memoization (Top-Down)
# Calculation: F(n) = F(n-1) + F(n-2)
# Time Complexity: O(n)
# Space Complexity: O(n)


def fib_memoization(n, memo=None):
    """
    Calculates the nth Fibonacci number starting from F(0) = 0, F(1) = 1.
    This is a recursive Top-Down approach with a dictionary cache.
    """
    if memo is None:
        memo = {}

    # Handle base cases
    if n <= 0:
        return 0
    if n == 1:
        return 1

    # Check the memo dictionary for pre-calculated results
    if n not in memo:
        memo[n] = fib_memoization(n - 1, memo) + fib_memoization(n - 2, memo)

    return memo[n]


if __name__ == "__main__":
    n = 6
    print(f"Fibonacci number at position {n} is: {fib_memoization(n)}")
    # Expected: F(0)=0, F(1)=1, F(2)=1, F(3)=2, F(4)=3, F(5)=5, F(6)=8
