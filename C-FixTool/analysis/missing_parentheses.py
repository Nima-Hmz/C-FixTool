def process_line(line):
    # Missing parentheses
    # Count open and close parentheses
    open_count = line.count("(")
    close_count = line.count(")")
    
    # Calculate the difference
    difference = open_count - close_count
    
    # If more open parentheses, add closing parentheses
    if difference > 0:
        line = line[:-1]
        line = line + ")" * difference
    
        # If line ends with a semicolon, move closing parentheses before the semicolon
        if line[-2] == ";":
            # Remove the semicolon temporarily
            line = line[:-2]
            # Add the necessary closing parentheses before the semicolon
            line = line + ")" * max(0, difference) + ";"
        
        # If line ends with a `{`, move closing parentheses before the `{`
        elif line[-2] == "{":
            # Add the necessary closing parentheses before the `{`
            line = line[:-2] + ")" * max(0, difference) + "{"
    
    # Return the fixed line
    return line