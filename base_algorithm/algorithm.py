import numpy as np

def levenshtein_distance(a, b):
    # Create a matrix to store distances
    n, m = len(a), len(b)
    dp = np.zeros((n + 1, m + 1), dtype=int)

    # Initialize base cases
    for i in range(n + 1):
        dp[i][0] = i
    for j in range(m + 1):
        dp[0][j] = j

    # Fill in the matrix
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            cost = 0 if a[i - 1] == b[j - 1] else 1
            dp[i][j] = min(dp[i - 1][j] + 1,  # Deletion
                           dp[i][j - 1] + 1,  # Insertion
                           dp[i - 1][j - 1] + cost)  # Substitution

    return dp[n][m]

def closest_match(word, keyword_list):
    closest_word = None
    min_distance = float('inf')

    # Find the closest word in the keyword list
    for keyword in keyword_list:
        distance = levenshtein_distance(word, keyword)
        if distance < min_distance:
            min_distance = distance
            closest_word = keyword

    return closest_word, min_distance

# Example usage
keywords = ["apple", "banana", "orange", "grape", "pineapple"]
word = "appl"
closest, distance = closest_match(word, keywords)
print(f"The closest match for '{word}' is '{closest}' with a distance of {distance}.")