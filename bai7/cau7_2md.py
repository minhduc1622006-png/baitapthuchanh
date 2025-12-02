# Minimal fix to the original structure

# Fix 1: Use unique variable names
file_handle = open('D:/a.txt', 'r') 
char, wc, lc = 0, 0, 0

for line in file_handle:
    # Fix 2: Increment line count immediately per loop iteration
    lc += 1
    
    # Strip the newline character for correct char and word counting (optional but cleaner)
    line = line.rstrip('\n') 
    
    # Fix 3: Use a unique variable (e.g., 'i') for the inner loop index
    for i in range(len(line)): 
        # Correct character counting
        char += 1
        
        # Fix 4: Counting words based on spaces
        if line[i] == ' ':
            wc += 1
    
    # Fix 5: Increment word count for the last word of the line 
    # (assuming the line is not empty after stripping '\n')
    if line.strip(): 
        wc += 1 

# Fix 6: Move print and close outside the loop
print("The no.of chars is %d\n The no.of words is %d\n The no.of lines is %d" % (char, wc, lc))

file_handle.close()
