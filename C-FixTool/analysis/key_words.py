import re

def process_line(line):
    # Complete the keywords
    new_line = line.split()
    final_line = ""
    c_keywords = [
    "auto", "break", "case", "char", "const", "continue", "default", "do", "double",
    "else", "enum", "extern", "float", "for", "goto", "if", "inline", "int", "long",
    "register", "restrict", "return", "short", "signed", "sizeof", "static", "struct",
    "switch", "typedef", "union", "unsigned", "void", "volatile", "while", "#include",
    "(", ')', '{', '}', '[', ']', ',', ';','"',"<stdio.h>", '=', '0', '1', '2', '3', '4', 
    '5', '6', '7', '8', '9', '0;'
    ]

    for word in new_line:
        closest, distance = closest_match(word, c_keywords)
        if distance < 2:
            for i in range(len(new_line)):
                if new_line[i] == word:
                    new_line[i] = closest
                    break  # Exit the loop once the item is replaced

    result = ' '.join(new_line)
    return result



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

# # Example usage
# keywords = ["apple", "banana", "orange", "grape", "pineapple"]
# word = "apple"
# closest, distance = closest_match(word, keywords)
# print(f"The closest match for '{word}' is '{closest}' with a distance of {distance}.")