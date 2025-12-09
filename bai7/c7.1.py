print("tran minh duc")
with open('a.txt', 'r') as input_file:
    for line in input_file:
        line = line.rstrip('\n')
        reversed_line = ""
        i = len(line)
        while i > 0:
            reversed_line += line[i - 1]
            i -= 1
        print(reversed_line)
