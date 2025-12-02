from itertools import islice # Placed at the top level

def file_read_from_head(fname, nlines):
    """
    Reads and prints the first nlines of a text file efficiently.
    """
    try:
        # Use 'with open' for safe file handling (defaults to 'r' mode)
        with open(fname, 'r') as f:
            # islice acts as a lazy slicer on the file iterator 'f'
            # It only reads up to nlines and then stops.
            for line in islice(f, nlines):
                # Print each line (must be indented inside the loop)
                print(line, end='') # Use end='' to prevent double-spacing 
                                    # since 'line' already contains a newline (\n)
    
    except FileNotFoundError:
        print(f"Error: File not found at {fname}")

# --- Example Usage (outside the function) ---
# This call reads and prints the first 2 lines from 'test.txt'
file_read_from_head('test.txt', 2)
