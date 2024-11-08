def compute_lps(pattern):
    """
    Computes the Longest Prefix Suffix (LPS) array for the given pattern.
    The LPS array stores the length of the longest proper prefix which is also a suffix.
    """
    m = len(pattern)
    lps = [0] * m  # Initialize LPS array
    length = 0     # Length of the previous longest prefix suffix
    i = 1          # Start from the second character

    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                # Consider the previous longest prefix suffix
                length = lps[length - 1]
                # Do not increment i here
            else:
                i += 1
    return lps

def kmp_search(text, pattern):
    """
    Performs KMP search of the pattern in the given text.
    Prints the starting indices where the pattern is found in the text.
    """
    n = len(text)
    m = len(pattern)

    if m == 0:
        print("Empty pattern provided.")
        return

    lps = compute_lps(pattern)  # Preprocess the pattern
    i = 0  # Index for text
    j = 0  # Index for pattern

    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == m:
            print(f"Pattern found at index: {i - j}")
            j = lps[j - 1]  # Continue searching for next possible match

        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

# Example Usage
if __name__ == "__main__":
    text = "BABABABABCABABCABAB"
    pattern = "ABABCABAB"
    kmp_search(text, pattern)
