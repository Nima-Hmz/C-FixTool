def process_line(line):
	# Missing Semicolons
  stripped_line = line.strip()
  
  # Skip lines that should not have a semicolon added
  if (
    not stripped_line or  # Empty lines
    stripped_line.startswith("#") or  # Preprocessor directives
    stripped_line.endswith(";") or  # Already ends with a semicolon
    stripped_line.endswith("{") or  # Opening brace for blocks
    stripped_line.endswith("}")  # Closing brace for blocks
  ):
    return line

  # Keywords that typically don't require a semicolon
  keywords = ["if", "else", "for", "while", "switch", "struct", "enum"]
  if any(stripped_line.startswith(kw) for kw in keywords):
    return line

  # Avoid adding a semicolon for function headers (e.g., `int add(int a, int b)`)
  # Heuristic: Check if the line contains `(` but not `);` and doesn't end with `{`
  if "(" in stripped_line and not stripped_line.endswith(");") and not stripped_line.endswith(") {"):
    return stripped_line + ';'

  # Add a semicolon if all conditions pass (for function calls, variable assignments, etc.)
  return stripped_line + ";"