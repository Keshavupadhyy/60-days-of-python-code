def fibonacci(n):
    """Function to generate the Fibonacci sequence."""
    fib_seq = [0, 1]
    for i in range(2, n):
        fib_seq.append(fib_seq[i-1] + fib_seq[i-2])
    return fib_seq

# Example usage:
n = 10
fib_seq = fibonacci(n)
print(f"The Fibonacci sequence up to {n} terms is: {fib_seq}")
