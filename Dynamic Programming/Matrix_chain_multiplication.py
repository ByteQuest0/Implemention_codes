def matrix_chain_multiplication(dimensions):

    n = len(dimensions) - 1  # Number of matrices

    # Initialize cost and split point matrices
    m = [[0] * n for _ in range(n)]  # Cost matrix
    s = [[0] * n for _ in range(n)]  # Split matrix

    # Fill the table for chain lengths 2 to n
    for l in range(1, n):  # l is the chain length
        for i in range(n - l):
            j = i + l
            m[i][j] = float('inf')

            # Try each possible split point
            for k in range(i, j):
                left_cost = m[i][k]
                right_cost = m[k + 1][j]
                mult_cost = dimensions[i] * dimensions[k + 1] * dimensions[j + 1]

                cost = left_cost + right_cost + mult_cost

                # Update if this split is better
                if cost < m[i][j]:
                    m[i][j] = cost
                    s[i][j] = k

    # Return the minimum cost and split info
    return m, s


def print_optimal_parenthesization(s, i, j, matrix_names):
    if i == j:
        return matrix_names[i]

    k = s[i][j]

    left = print_optimal_parenthesization(s, i, k, matrix_names)
    right = print_optimal_parenthesization(s, k + 1, j, matrix_names)

    return f"({left}{right})"


# Example usage
if __name__ == "__main__":
    # Example: A(2x3), B(3x4), C(4x5), D(5x6)
    dimensions = [2, 3, 4, 5, 6]
    matrix_names = ["A", "B", "C", "D"]

    m, s = matrix_chain_multiplication(dimensions)

    print(f"Optimal multiplication cost: {m[0][len(matrix_names) - 1]}")
    print(f"Optimal parenthesization: {print_optimal_parenthesization(s, 0, len(matrix_names) - 1, matrix_names)}")
