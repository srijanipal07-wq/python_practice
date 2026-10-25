# Star Pattern
def print_star_pattern(n):
    for i in range(n):
        print(" " * (n - i - 1) + "*" * (2 * i + 1))

# Example usage
print_star_pattern(5)