# Function 1: Using a simple slice for reversal (Most Pythonic)

def reverse_file_content_slice(file_path):
    # Use 'with open' to ensure the file is automatically closed, 
    # even if errors occur (This is best practice).
    with open(file_path, 'r') as input_file:
        for line in input_file:
            # Strip trailing newline characters first (optional but recommended)
            line = line.rstrip('\n') 
            
            # String Slicing: [start:stop:step] where -1 step reverses the string.
            reversed_line = line[::-1]
            
            print(reversed_line)

# Example usage:
# reverse_file_content_slice('D:/a.txt')
