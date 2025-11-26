class py_solution:
    def roman_to_int(self, s):
        if not isinstance(s, str):
            raise TypeError("Input must be a string.")

        s = s.strip().upper()
        if s == "":
            return 0

        rom_val = { 'I': 1, 'V': 5, 'X': 10,
                    'L': 50, 'C': 100, 'D': 500, 'M': 1000 }
        for ch in s:
            if ch not in rom_val:
                raise ValueError(f"Invalid Roman numeral character: {ch}")

        int_val = 0
        for i in range(len(s)):
            if i > 0 and rom_val[s[i]] > rom_val[s[i - 1]]:
                int_val += rom_val[s[i]] - 2 * rom_val[s[i - 1]]
            else:
                int_val += rom_val[s[i]]

        return int_val
solver = py_solution()
print(solver.roman_to_int('MMMCMXLXXXVI'))
print(solver.roman_to_int('mmmm'))
print(solver.roman_to_int('C'))

